from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

	def setUp(self):
		self.browser = webdriver.Firefox()
		
	def tearDown(self):
		self.browser.quit()
		
	def test_correct_titles(self):
		#Blog Page
		self.browser.get('http://localhost:8000')
		self.assertIn('Trevor\'s Django Blog', self.browser.title)
		
		#CV Page
		self.browser.get('http://localhost:8000/cv/')
		self.assertIn('Trevor\'s Django CV', self.browser.title)
		
		personal_details_header_text = self.browser.find_element_by_class_name('personal-detail-header').text
		self.assertIn('Personal Details', personal_details_header_text)
		
		personal_statement_header_text = self.browser.find_element_by_class_name('personal-statement-header').text
		self.assertIn('Personal Statement', personal_statement_header_text)
		
		education_header_text = self.browser.find_element_by_class_name('education-header').text
		self.assertIn('Education', education_header_text)
		
		work_experience_header_text = self.browser.find_element_by_class_name('work-experience-header').text
		self.assertIn('Work Experience', work_experience_header_text)
		
		personal_interests_header_text = self.browser.find_element_by_class_name('personal-interests-header').text
		self.assertIn('Personal Interests', personal_interests_header_text)
		
if __name__ == '__main__':
	unittest.main(warnings='ignore')