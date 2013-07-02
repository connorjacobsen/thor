# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from django.views import generic
from django.contrib.auth.decorators import login_required

from succinctly.models import Article

def index(request):
	if request.user.is_authenticated():
		user_is_loggedin = True
		user = request.user # get the user
	else:
		user_is_loggedin = False	
		user = request.user
	article_list = Article.objects.order_by('-pub_date')#[:20]
	"""Return last 10 published articles."""
	return render(request, 'succinctly/index.html', {'article_list': article_list, 'user_is_loggedin': user_is_loggedin, 'user':user})

@login_required
def detail(request, article_id):
	article = get_object_or_404(Article, pk=article_id) # Get the article specified by the url
	return render(request, 'succinctly/detail.html', {'article': article})



def home(request):
	user = request.user # Get the current user
	return render(request, 'succinctly/home.html', {'user': user})	