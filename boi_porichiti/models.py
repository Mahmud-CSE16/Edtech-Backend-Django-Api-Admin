from django.db import models

from common.models import SubCategory

# Create your models here.

class Boi(models.Model):
    title = models.CharField(max_length=255)
    cover_img = models.FileField(upload_to='boi_porichiti/cover')
    description = models.TextField(blank=True,null=True)
    pdf_file = models.FileField(upload_to='boi_porichiti/pdf')
    subcategories = models.ManyToManyField(SubCategory,blank=True)

    class Meta:
        ordering = ('title',)
        verbose_name = "বই পরিচিতি" 
        verbose_name_plural = "বই পরিচিতি"
        