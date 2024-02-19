import re
from django.shortcuts import render
from .models import Post
from django.utils import timezone 
from django.urls import reverse
from django.http import HttpResponseRedirect
import sweetify 

# Create your views here.


def blog_home_view(request):
    posts = Post.objects.filter(status=True).order_by('-created_date')
    context = {'posts': posts}
    return render(request , 'blog/blog.html' , context)

def blog_single(request,pid):
    pass 