from django.urls import path,include
from .views import * 


app_name = 'blog'

urlpatterns = [
    path('',blog_home_view,name='index'),
    path('<int:pid>' , blog_single , name='post-detail'),
    path('author/<str:author_username>', blog_home_view , name='author'),
    path('category/<str:cat_name>',blog_home_view , name='category'),
    path('tag/<str:tag_name>',blog_home_view,name='tag'),
    path('search/',blog_search,name='search'),

]








