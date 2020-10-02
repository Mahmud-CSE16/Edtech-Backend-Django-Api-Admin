from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

from common.models import SubCategory

# Create your models here.

class Boi(models.Model):
    published = models.BooleanField(default=True)
    title = models.CharField(max_length=255)
    cover_img = models.ImageField(upload_to='boi_porichiti/cover')
    description = RichTextUploadingField(blank=True,null=True)
    pdf_file = models.FileField(upload_to='boi_porichiti/pdf',blank=True, null=True)
    subcategories = models.ManyToManyField(SubCategory,blank=True)

    class Meta:
        ordering = ('title',)
        verbose_name = "বই পরিচিতি" 
        verbose_name_plural = "বই পরিচিতি"
        