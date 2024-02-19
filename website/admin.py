from django.contrib import admin
from .models import Contact 


class ContactAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = "-empty-"
    list_display = ('name', 'email', 'subject', 'created_date')
    list_filter = ('subject',)
    search_fields = ('name', 'subject' , 'email')




# Register your models here.
admin.site.register(Contact, ContactAdmin)