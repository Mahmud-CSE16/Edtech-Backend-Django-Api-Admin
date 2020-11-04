from django.contrib import admin
from .models import Notification

# Register your models here.
@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('title','created_time_format','published_time_format','published',)
    list_editable = ('published',)
    list_filter = ('subCategories','published',)
    search_fields = ('title','short_description','long_description',)
    fieldsets = [
        (None,{
            'fields':('subCategories','title','short_description','long_description','published',),
        }),
    ]

    def published_time_format(self, obj):
        if(obj.published_time == None):
            return "Not Published"
        return obj.published_time.strftime("%d-%b-%Y %H:%M:%S")
    published_time_format.short_description = 'Published Time'

    def created_time_format(self, obj):
        return obj.created_time.strftime("%d-%b-%Y %H:%M:%S")
    created_time_format.short_description = 'Created Time'
    
