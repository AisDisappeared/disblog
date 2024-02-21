import re
from django.shortcuts import render,redirect,get_object_or_404
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
    now = timezone.now()
    all_posts = Post.objects.filter(status=True,published_date__lte=now)
    current_index = 0 

    for i , post in enumerate(all_posts):
        if post.id == pid:
            current_index = i 
            break 
    
    prev_post = all_posts[current_index - 1] if current_index - 1 >= 0 else None 
    next_post = all_posts[current_index + 1] if current_index + 1 < len(all_posts) else None
    current_post = get_object_or_404(all_posts , pk = pid) 
    context = {'post' : current_post, 'prev_post' : prev_post , 'next_post' : next_post}
    return render(request , 'blog/post-details.html', context)  

