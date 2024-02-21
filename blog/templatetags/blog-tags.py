from atexit import register
from django import template
from django.utils import timezone
from blog.models import Post

# register the django custom template tag python file 
register = template.Library()



@register.inclusion_tag('blog/blog-recent-posts.html')
def recent_posts():
    now = timezone.now()
    posts = Post.objects.filter(status=True,published_date__lt=now).order_by('-published_date')[:3]
    return {'posts':posts}
   