# Create your views here.

from django.shortcuts import render
from django.http import HttpResponse
from blog.models import User
from blog.models import Post

def home(request):
	#context = RequestContext(request)
	return HttpResponse("Testing")