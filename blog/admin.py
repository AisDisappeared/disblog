from django.contrib import admin
from .models import Post , Category
# Register your models here.


class PostAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = "-empty-"
    list_display = ('title', 'author', 'status', 'published_date', 'login_required')
    list_filter = ('author','categories','tags')
    search_fields = ('name', 'subject' , 'email')



admin.site.register(Category)
admin.site.register(Post, PostAdmin)