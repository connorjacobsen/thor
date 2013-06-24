"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""
import datetime

from django.utils import timezone
from django.test import TestCase
from django.core.urlresolvers import reverse

from succinctly.models import Article


class ArticleMethodTests(TestCase):
	def test_was_published_recently_with_future_article(self):
		"""
		was_published_recently() should return False for articles whose 
		pub_date is in the future.
		"""
		future_article = Article(pub_date=timezone.now() + datetime.timedelta(days=30))
		self.assertEqual(future_article.was_published_recently(), False)

	def test_was_published_recently_with_old_article(self):
		"""
		was_published_recently() should return False for articles whose pub_date
		is older than one day
		"""
		old_article = Article(pub_date=timezone.now() - datetime.timedelta(days=30))
		self.assertEqual(old_article.was_published_recently(), False)

	def test_was_published_recently_with_recent_article(self):
		"""
		was_published_recently() should return True for articles whose pub_date
		is within the last day
		"""
		recent_article = Article(pub_date=timezone.now() - datetime.timedelta(hours=1))
		self.assertEqual(recent_article.was_published_recently(), True)		

def create_article(summary, days):
	"""
	Creates an article with the given 'summary' published the given numbers of 
	'days' offset to now (negative for articles published in the past,
	positive for articles that have yet to be published).
	"""
	return Article.objects.create(summary=summary, pub_date=timezone.now() + datetime.timedelta(days=days))


class ArticleViewTests(TestCase):
	def test_index_view_with_no_articles(self):
		"""
		If no articles exist, an appropriate message should be displayed
		"""
		response = self.client.get(reverse('succinctly:index'))
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, "No summaries are available.")
		self.assertQuerysetEqual(response.context['article_list'], [])

	def test_index_view_with_a_past_article(self):
		"""
		Articles with a pub_date in the past should be displayed on the index page.
		"""
		create_article(summary="Past article.", days=-30)
		response = self.client.get(reverse('succinctly:index'))
		self.assertQuerysetEqual(
			response.context['article_list'],
			['<Article: Past article.>']
		)

	def test_index_view_with_a_future_article(self):
		"""
		Articles with a pub_date in the future should not be displayed on the
		index page.
		"""
		create_article(summary="Future article.", days=30)
		response = self.client.get(reverse('succinctly:index'))
		self.assertContains(response, "No summaries are available.", status_code=200)
		self.assertQuerysetEqual(response.context['article_list'],[])

	def test_index_view_with_future_article_and_past_article(self):
		"""
		Even if both past and future articles exist, only past articles should be 
		displayed.
		"""
		create_article(summary="Past article", days=-30)
		create_article(summary="Future article.", days=30)
		response = self.client.get(reverse('succinctly:index'))
		self.assertQuerysetEqual(
			response.context['article_list'],
			['<Article: Past article.>']
		)

	def test_index_view_with_two_past_polls(self):
		create_article(summary="Past article 1.", days=-20)
		create_article(summary="Past article 2.", days=-65)
		response = self.client.get(reverse('succinctly:index'))
		self.assertQuerysetEqual(
			response.context['article_list'],
			['<Article: Past article 2.>', '<Article: Past article 1.>']
		)		