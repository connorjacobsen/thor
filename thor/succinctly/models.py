import datetime
from django.db import models
from django.utils import timezone

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
	# Django will automcatically give it an 'id' attribute

	def __unicode__(self):
		return self.summary # display the summary in the admin instead of 'object'

	def was_published_recently(self):
		now = timezone.now()
		return now - datetime.timedelta(days=1) <= self.pub_date < now