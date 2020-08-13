from django.db import models
from common.models import SubCategory,QuestionHistory

# Create your models here.

class BigotoBochor(models.Model):
    question_history = models.ForeignKey(QuestionHistory,on_delete=models.CASCADE)
    subcategory = models.ForeignKey(SubCategory,on_delete=models.CASCADE)
    pdf_file = models.FileField(upload_to='bigotobochor')

    class Meta:
        ordering = ('-question_history__year','question_history__board__name','subcategory__name',)