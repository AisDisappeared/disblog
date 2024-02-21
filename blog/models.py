from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager


# Create your models here.



#  category model 
class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name 







#  post model 
class Post(models.Model):
    
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    content = models.TextField()
    image = models.ImageField(upload_to='blog/',default='blog/default2.jpg')
    status = models.BooleanField(default=True)
    tags = TaggableManager()
    categories = models.ManyToManyField(Category)
    login_required = models.BooleanField(default=False)
    counted_views = models.IntegerField(default=0)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    published_date = models.DateTimeField(null=True)
    

    class Meta:
        ordering = ['-created_date']
    
    def __str__(self):
       return '{}'.format( self.id)
    


# class Comments
    