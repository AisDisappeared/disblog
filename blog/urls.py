from django.urls import path,include
from .views import * 


app_name = 'blog'

urlpatterns = [
    path('',blog_home_view,name='index'),
]
