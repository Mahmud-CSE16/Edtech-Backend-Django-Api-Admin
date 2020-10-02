from django.contrib import admin
from django.conf import settings

from .models import Boi
from django.utils.safestring import mark_safe

# Register your models here.

@admin.register(Boi)
class BigotoBochorAdmin(admin.ModelAdmin):
    list_display = ('cover_img_view','title','embed_pdf_file','published',)
    list_editable = ('published',)
    list_display_links =('cover_img_view','title',)
    list_filter = ('subcategories',)
    search_fields = ('title','subcategories__name')
    list_per_page = 25

    # profile pic
    def cover_img_view(self,obj):
        print(obj.cover_img)
        if(obj.cover_img != None and obj.cover_img != "" ):
            return mark_safe('<img src="%s/media/%s" width="50" height="50" />' % (settings.SITE_DOMAIN,obj.cover_img))
        else:
            return mark_safe('<img src="/static/img/cover.jpg" width="50" height="50" />')

    cover_img_view.short_description = 'Cover Image'

    # pdf file
    def embed_pdf_file(self,obj):
        if(obj.pdf_file != None and obj.pdf_file != "" ):
            # return mark_safe('<embed src="/pdf/?url={0}" type="application/pdf" width="100%" height="300px"/>'.format(obj.pdf_file.url,))
            return mark_safe('<a href="/pdf/?url={0}">Show PDF</a>'.format(obj.pdf_file.url,))
    
    embed_pdf_file.short_description = "PDF File"


