from django.contrib import admin
from .models import BigotoBochor
from django.utils.safestring import mark_safe
from django.utils.html import format_html

# Register your models here.

@admin.register(BigotoBochor)
class BigotoBochorAdmin(admin.ModelAdmin):
    list_display = ('question_history','subcategory','embed_pdf_file',)
    # list_editable = ('published',)
    list_filter = ('subcategory','question_history__board__name','question_history__year',)
    search_fields = ('question_history__year','question_history__board__name')
    list_per_page = 25

    # def embed_pdf_file(self, obj):
    #     # check for valid URL and return if no valid URL
    #     url = obj.pdf_file.url
    #     html = '<embed src="{url}" type="application/pdf">'
    #     formatted_html = format_html(html.format(url=obj.pdf_file.url))
    #     return formatted_html

    # pdf file
    def embed_pdf_file(self,obj):
        if(obj.pdf_file != None and obj.pdf_file != "" ):
            #return mark_safe('<embed src="/pdf/?url={0}" type="application/pdf" width="100%" height="300px"/>'.format(obj.pdf_file.url,))
            return mark_safe('<a href="/pdf/?url={0}">Show PDF</a>'.format(obj.pdf_file.url,))
        
    embed_pdf_file.short_description = 'Question'
