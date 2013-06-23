# Create your views here.
from django.http import HttpResponse

def index(request):
	return HttpResponse('Hello, world!')

def detail(request, article_id):
	return HttpResponse("You are looking at article %s." % article_id)	