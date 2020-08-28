from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.
class PersonalDetails(models.Model):
	first_name = models.CharField(max_length=200)
	last_name = models.CharField(max_length=200)
	email = models.EmailField(max_length=200)
	mobile_number = models.CharField(max_length=200)
	
	def __str__(self):
		return self.first_name
		
class PersonalStatement(models.Model):
	author = models.CharField(max_length=200)
	text = models.TextField()
	
	def __str__(self):
		return self.author

class PersonalInterests(models.Model):
	author = models.CharField(max_length=200)
	text = models.TextField()
	
	def __str__(self):
		return self.author

class Education(models.Model):
	establishment_name = models.CharField(max_length=200)
	establishment_address = models.CharField(max_length=200)
	started_date = models.DateTimeField(blank=True, null=True)
	finished_date =  models.DateTimeField(blank=True, null=True)
	text = models.TextField()
	
	def __str__(self):
		return self.establishment_name

class WorkExperience(models.Model):
	establishment_name = models.CharField(max_length=200)
	establishment_address = models.CharField(max_length=200)
	establishment_email = models.CharField(max_length=200, blank=True, null=True)
	started_date = models.DateTimeField(blank=True, null=True)
	finished_date =  models.DateTimeField(blank=True, null=True)
	text = models.TextField()
	
	def __str__(self):
		return self.establishment_name