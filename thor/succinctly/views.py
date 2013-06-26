# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from django.views import generic

from succinctly.models import Article

class IndexView(generic.ListView):
	template_name = 'succinctly/index.html'
	context_object_name = 'article_list'

	def get_queryset(self):
		"""Return last 10 published articles."""
		return Article.objects.order_by('-pub_date')[:10]

class DetailView(generic.DetailView):
	model = Article
	template_name = 'succinctly/detail.html'