import re
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .forms import ContactForm
from django.contrib import messages 
import sweetify
# Create your views here.




# index home view function 
def index_view(request):
   return render(request , 'website/index.html')



# about view function
def about_view(request):
   return render(request , 'website/about.html')



# contact view
def contact_view(request):
   if request.method == 'POST':
      form = ContactForm(request.POST)
      if form.is_valid():
         form.save()
         sweetify.success(request, 'your message has been sent')
      else:
         sweetify.error(request,'your ticket doesn\'t post',persistent=':(')
   form = ContactForm(request.POST)
   context = {'form': form}
   return render(request , 'website/contact.html',context)

