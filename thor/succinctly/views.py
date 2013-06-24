# Create your views here.
from django.shortcuts import render, get_object_or_404

from succinctly.models import Article

def index(request):
	article_list = Article.objects.order_by('-pub_date')[:10]
	context = {'article_list': article_list}
	return render(request, 'succinctly/index.html', context)

def detail(request, article_id):
	article = get_object_or_404(Article, pk=article_id)
	return render(request, 'succinctly/detail.html', {'article': article})	