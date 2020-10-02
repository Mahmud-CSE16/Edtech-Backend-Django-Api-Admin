from django.contrib import admin
from django.conf import settings

from .models import Blog
from django.utils.safestring import mark_safe

# Register your models here.

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('cover_img_view','title','created_time','published',)
    list_editable = ('published',)
    list_display_links =('cover_img_view','title',)
    list_filter = ('created_time',)
    search_fields = ('title',)
    list_per_page = 25

    # profile pic
    def cover_img_view(self,obj):
        print(obj.cover_img)
        if(obj.cover_img != None and obj.cover_img != "" ):
            return mark_safe('<img src="%s/media/%s" width="50" height="50" />' % (settings.SITE_DOMAIN,obj.cover_img))
        else:
            return mark_safe('<img src="/static/img/cover.jpg" width="50" height="50" />')

    cover_img_view.short_description = 'Cover Image'

