from django.urls import path,include
from .views import * 


urlpatterns = [
    path('',index_view,name='index'),
    path('about' , about_view ,name='about'),
    path('contact' , contact_view,name="contact"),
]
