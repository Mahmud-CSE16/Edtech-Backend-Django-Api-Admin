from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


from common.models import SubCategory

# Create your models here.

class Shop(models.Model):
    published = models.BooleanField(default=True)
    title = models.CharField(max_length=255)
    cover_img = models.ImageField(upload_to='shop/cover')
    description = RichTextUploadingField(blank=True,null=True)
    pdf_file = models.FileField(upload_to='shop/pdf',blank=True, null=True)
    subcategories = models.ManyToManyField(SubCategory,blank=True)

    class Meta:
        ordering = ('title',)
        verbose_name = "দোকান" 
        verbose_name_plural = "দোকান"
        