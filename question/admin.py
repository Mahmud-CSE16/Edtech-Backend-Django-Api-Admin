from django.contrib import admin
from .models import McqQuestion


# Register your models here.
@admin.register(McqQuestion)
class McqQuestionAdmin(admin.ModelAdmin):
    list_display = ('id','question_body_field','published')
    list_editable = ('published',)
    list_display_links = ('id','question_body_field',)
    list_filter = ('published','subcategories','chapters','histories','types','language',)
    search_fields = ('id','question_body','language__name','subcategories__name','chapters__name','histories__year','histories__board__name','types__name',)
    list_per_page = 25
