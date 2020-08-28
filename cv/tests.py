from datetime import datetime
from django.utils.timezone import get_current_timezone
from django.test import TestCase
from django.urls import resolve
from django.contrib.auth.models import User

from cv.models import PersonalDetails, PersonalStatement, Education, WorkExperience, PersonalInterests

from blog.views import post_list


# Create your tests here.
class SmokeTest(TestCase):
	#Deliberate fail test, carried from tutorial to ensure tests are being done properly
	
	def test_bad_maths(self):
		self.assertEqual(1+1,3)
		
class HomePageTest(TestCase):

	def test_root_url_resolves_to_blog_view(self):
		found = resolve('/')
		
		self.assertEqual(found.func, post_list)
		
	def test_can_switch_to_cv_view(self):
		response = self.client.get('/cv/')
		
		self.assertTemplateUsed(response, 'cv/base.html')
		self.assertTemplateUsed(response, 'cv/cv_list.html')
		
	def test_home_page_returns_correct_html(self):
		response = self.client.get('/')
		
		self.assertTemplateUsed(response, 'blog/base.html')
		self.assertTemplateUsed(response, 'blog/post_list.html')
		
	def test_personal_details_display(self):
		PersonalDetails.objects.create(first_name='FirstName', last_name='LastName', email='Test@gmail.com', mobile_number='0123456789')
		
		response = self.client.get('/cv/')
		html = response.content.decode()
		
		self.assertIn('FirstName', html)
		self.assertIn('LastName', html)
		self.assertIn('Test@gmail.com', html)
		self.assertIn('0123456789', html)
		
	def test_personal_statement_display(self):
		PersonalStatement.objects.create(author='StatementAuthor', text='StatementText')
		response = self.client.get('/cv/')
		
		self.assertIn('StatementText', response.content.decode())
		
	def test_education_display(self):
		dateTimeFiller = datetime.now(tz=get_current_timezone())
		Education.objects.create(establishment_name='School', establishment_address='School Location', started_date=dateTimeFiller, finished_date=dateTimeFiller, text='School Desc')
		
		response = self.client.get('/cv/')
		html = response.content.decode()
		
		self.assertIn('School', html)
		self.assertIn('School Location', html)
		self.assertEqual(dateTimeFiller, Education.objects.first().started_date)
		self.assertEqual(dateTimeFiller, Education.objects.first().finished_date)
		self.assertIn('School Desc', html)
		
	def test_work_experience_display(self):
		dateTimeFiller = datetime.now(tz=get_current_timezone())
		WorkExperience.objects.create(establishment_name='Job', establishment_address='Job Location', establishment_email='job@gmail.com', started_date=dateTimeFiller, finished_date=dateTimeFiller, text='Job Desc')
		
		response = self.client.get('/cv/')
		html = response.content.decode()
		
		self.assertIn('Job', html)
		self.assertIn('Job Location', html)
		self.assertIn('job@gmail.com', html)
		self.assertEqual(dateTimeFiller, WorkExperience.objects.first().started_date)
		self.assertEqual(dateTimeFiller, WorkExperience.objects.first().finished_date)
		self.assertIn('Job Desc', html)
		
	def test_personal_interests_display(self):
		PersonalInterests.objects.create(author='InterestsAuthor', text='InterestsText')
		response = self.client.get('/cv/')
		
		self.assertIn('InterestsText', response.content.decode())
		
	def test_user_authentication(self):
		user = User.objects.create(username='Test')
		user.set_password('TestPassword')
		user.save()
		self.assertTrue(self.client.login(username='Test', password='TestPassword'))
		
	
		
		