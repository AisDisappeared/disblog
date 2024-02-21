import re
from django.shortcuts import render,redirect,get_object_or_404
from .models import Post
from django.utils import timezone 
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
import sweetify 

# Create your views here.



# all blog posts view
def blog_home_view(request,author_username=None,cat_name=None):
    now = timezone.now()
    posts = Post.objects.filter(status=True,published_date__lte=now).order_by('-created_date')
    if author_username:
        posts = posts.filter(author__username=author_username)
    if cat_name:
        posts = posts.filter(categories__name=cat_name)
    p = Paginator(posts,4)
    try:
        page_number = request.GET.get('page')
        posts = p.get_page(page_number)
    except EmptyPage:
        posts = posts.get_page(1)
    except PageNotAnInteger:
        posts = posts.get_page(1)

    context = {'posts': posts}
    return render(request , 'blog/blog.html' , context)






# blog single view
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
    current_post.counted_views += 1 
    current_post.save()
    context = {'post' : current_post, 'prev_post' : prev_post , 'next_post' : next_post}
    return render(request , 'blog/post-details.html', context)  

