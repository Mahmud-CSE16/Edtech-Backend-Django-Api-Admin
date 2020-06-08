from django.contrib import admin
from .models import Category,SubCategory,Chapter,Language,Board,QuestionHistory,QuestionType,Question


# Register your models here.
admin.site.register(Category)
admin.site.register(Language)
admin.site.register(Board)
admin.site.register(QuestionType)

@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ('name','category',)
    list_filter = ('category',)
    search_fields = ('name','category__name',)


@admin.register(Chapter)
class ChapterAdmin(admin.ModelAdmin):
    list_display = ('name','subcategory',)
    list_filter = ('subcategory',)
    search_fields = ('name','subcategory__name',)
    list_per_page = 25


@admin.register(QuestionHistory)
class QuestionAdmin(admin.ModelAdmin):
    list_filter = ('board','year')
    list_per_page = 25


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_body_field','published')
    list_editable = ('published',)
    list_filter = ('published','subcategories','chapters','histories','types','language',)
    search_fields = ('question_body','language__name','subcategories__name','chapters__name','histories__year','histories__board__name','types__name',)
    list_per_page = 25
