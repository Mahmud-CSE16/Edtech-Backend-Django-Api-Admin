from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


from common.models import SubCategory

# Create your models here.

class GoniterItihash(models.Model):
    title = models.CharField(max_length=255)
    cover_img = models.ImageField(upload_to='shop/cover')
    description = RichTextUploadingField(blank=True,null=True)

    class Meta:
        ordering = ('title',)
        verbose_name = "গনিতের ইতিহাস" 
        verbose_name_plural = "গনিতের ইতিহাস"
        