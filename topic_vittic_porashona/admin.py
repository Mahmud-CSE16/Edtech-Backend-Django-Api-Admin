from django.contrib import admin
from django.utils.safestring import mark_safe
from django.conf import settings
from .models import TopicVitticPorashona


# Register your models here.
@admin.register(TopicVitticPorashona)
class TopicVitticPorashonaAdmin(admin.ModelAdmin):
    list_display = ('cover_img_view','title','topic_number','published')
    list_editable = ('published','topic_number')
    list_display_links = ('cover_img_view','title')
    list_filter = ('published','subcategories','chapters',)
    search_fields = ('topic_number','title','subcategories__name','chapters__name',)
    list_per_page = 25

    # profile pic
    def cover_img_view(self,obj):
        print(obj.cover_img)
        if(obj.cover_img != None and obj.cover_img != "" ):
            return mark_safe('<img src="%s/media/%s" width="50" height="50" />' % (settings.SITE_DOMAIN,obj.cover_img))
        else:
            return mark_safe('<img src="/static/img/cover.jpg" width="50" height="50" />')

    cover_img_view.short_description = 'Cover Image'
