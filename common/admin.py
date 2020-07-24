from django.contrib import admin
from .models import Category,SubCategory,Chapter,Language,Board,QuestionHistory,QuestionType

# Register your models here.
admin.site.register(Language)
admin.site.register(Board)
admin.site.register(QuestionType)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name','published',)
    list_editable = ('published',)
    list_filter = ('published',)
    search_fields = ('name',)

@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ('name','number_of_questions_for_mcq_exam','category','published',)
    list_editable = ('published',)
    list_filter = ('category','published')
    search_fields = ('name','category__name',)


@admin.register(Chapter)
class ChapterAdmin(admin.ModelAdmin):
    list_display = ('name','subcategory','published')
    list_editable = ('published',)
    list_filter = ('subcategory','published')
    search_fields = ('name','subcategory__name',)
    list_per_page = 25


@admin.register(QuestionHistory)
class QuestionHistoryAdmin(admin.ModelAdmin):
    list_filter = ('board','year')
    list_per_page = 25
