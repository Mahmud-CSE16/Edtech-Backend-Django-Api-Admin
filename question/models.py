from django.db import models
import datetime
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils.safestring import mark_safe
from ckeditor_uploader.fields import RichTextUploadingField
from common.models import SubCategory,Chapter,Language,QuestionHistory,QuestionType

# Create your models here.

"""Question"""
options = [
    (1,1), (2,2), (3,3),(4,4),
]
class McqQuestion(models.Model):
    published = models.BooleanField(default=False)
    question_body = RichTextUploadingField()
    option1 = RichTextUploadingField()
    option2 = RichTextUploadingField()
    option3 = RichTextUploadingField()
    option4 = RichTextUploadingField()
    answer_number = models.PositiveIntegerField(choices=options,validators=[MinValueValidator(1), MaxValueValidator(4)])
    solution = RichTextUploadingField()
    subcategories = models.ManyToManyField(SubCategory)
    chapters = models.ManyToManyField(Chapter)
    language = models.ForeignKey(Language, on_delete=models.CASCADE,default=1)
    histories = models.ManyToManyField(QuestionHistory,blank=True)
    types = models.ManyToManyField(QuestionType)


    def __str__(self):
        return mark_safe(self.question_body)

    def question_body_field(self):
            return mark_safe(self.question_body)

    question_body_field.short_description = 'Question Body'
