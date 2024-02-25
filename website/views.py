import re
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .forms import ContactForm
from django.contrib import messages 
from blog.models import Post
from django.utils import timezone
import sweetify
# Create your views here.




# index home view function 
def index_view(request):
   now = timezone.now()
   posts = Post.objects.filter(status=True,published_date__lte=now).order_by('-created_date')[:3]
   context = {'posts': posts}
   return render(request , 'website/index.html' , context)



# about view function
def about_view(request):
   return render(request , 'website/about.html')



# contact view
def contact_view(request):
   if request.method == 'POST':
      form = ContactForm(request.POST)
      if form.is_valid():
         form.save()       
         sweetify.success(request,'your message has been sent',persistent = 'OK')
      else:
         sweetify.error(request,'your ticket doesn\'t  post',persistent = ':(')

         
   form = ContactForm(request.POST)
   context = {'form': form}
   return render(request , 'website/contact.html',context)

