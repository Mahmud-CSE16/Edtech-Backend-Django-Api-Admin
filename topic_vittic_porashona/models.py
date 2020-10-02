from django.db import models
import datetime
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils.safestring import mark_safe
from ckeditor_uploader.fields import RichTextUploadingField
from common.models import SubCategory,Chapter,Language,QuestionHistory,QuestionType
from question.models import McqQuestion

# Create your models here.

class TopicVitticPorashona(models.Model):
    published = models.BooleanField(default=True)
    topic_number = models.IntegerField()
    title = models.CharField(max_length=255)
    cover_img = models.ImageField(upload_to='shop/cover')
    description = RichTextUploadingField()
    chapters = models.ManyToManyField(Chapter,)
    subcategories = models.ManyToManyField(SubCategory,blank=True)
    questions = models.ManyToManyField(McqQuestion,) 

    class Meta:
        ordering = ('topic_number',)
        verbose_name = "Topic" 
        verbose_name_plural = "Topics"
