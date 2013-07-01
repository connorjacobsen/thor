import datetime
from django.db import models
from django.utils import timezone

# Create website to use as foreign key
class Website(models.Model):
	# The websites name:
	name = models.CharField(max_length=30)
	# The website's url
	url = models.URLField(max_length=254)
	# Website's image link url
	logo_image_url = models.URLField(max_length=254) 

	def __unicode__(self):
		return self.name 

# Create your models here.
class Article(models.Model):
	# url of original Article
	full_URL = models.URLField(max_length=200)
	# summary itself
	summary = models.TextField(max_length=140)
	# author's name?
	author = models.CharField(max_length=30)
	# website the article came from (ie. TechCrunch)
	webpage_name = models.CharField(max_length=35)
	# the article's timestamp
	pub_date = models.DateTimeField(auto_now=False, auto_now_add=False)

	# url of the image associated with the article 
	image_url = models.URLField(max_length=254, blank=True)
	# Django will automcatically give it an 'id' attribute

	# Website foreign key
	home_site = models.ForeignKey(Website, blank=True, null=True, on_delete=models.SET_NULL)

	def __unicode__(self):
		return self.summary # display the summary in the admin instead of 'object'

	def was_published_recently(self):
		now = timezone.now()
		return now - datetime.timedelta(days=1) <= self.pub_date < now

# class CustomUser(AbstractBaseUser):
