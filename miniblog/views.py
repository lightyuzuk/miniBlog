#coding:utf-8

from django.shortcuts import render, render_to_response
from django.http import HttpResponse

from miniblog.models import *

def home(request):
	'''home'''
	myBlog = Blog.objects.get(id=1)
	return render(request,'index.html',locals())