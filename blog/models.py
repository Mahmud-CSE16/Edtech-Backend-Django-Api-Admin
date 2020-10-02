from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


from common.models import SubCategory
from datetime import datetime

# Create your models here.

class Blog(models.Model):
    published = models.BooleanField(default=True)
    title = models.CharField(max_length=255)
    cover_img = models.ImageField(upload_to='blog/cover')
    description = RichTextUploadingField(blank=True,null=True)
    created_time = models.DateTimeField(default = datetime.now)

    class Meta:
        ordering = ('-created_time',)
        verbose_name = "Blog" 
        verbose_name_plural = "Blogs"
        