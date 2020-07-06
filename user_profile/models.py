from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

from common.models import Category,SubCategory
from django.utils.safestring import mark_safe



class District(models.Model):
    name = models.CharField(max_length=25,unique=True)


    class Meta:
        ordering = ('name', )

    def __str__(self):
        return self.name

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    uid = models.CharField(max_length=255,unique=True,blank=True)
    device_token = models.CharField(max_length=255,blank=True)
    name = models.CharField(max_length=255,blank=True)
    email = models.CharField(max_length=255, blank=True)
    profile_pic_url = models.URLField(max_length=500,blank=True)
    phone = models.CharField(max_length=15,blank=True)
    dateOfBirth = models.DateField(blank=True,null=True)
    address = models.CharField(max_length=255,blank=True)
    institute = models.CharField(max_length=255,blank=True)
    level = models.ForeignKey(Category,on_delete=models.CASCADE)
    sub_level = models.ForeignKey(SubCategory,on_delete=models.CASCADE)
    district = models.ForeignKey(District, on_delete=models.CASCADE)

    class Meta:
        ordering = ('name', )


    def __str__(self):
        return self.name

    def profile_image(self):
        if(self.profile_pic_url != None and self.profile_pic_url != "" ):
            return mark_safe('<img src="%s" width="50" height="50" />' % (self.profile_pic_url))
        else:
            return mark_safe('<img src="/static/img/user_icon.png" width="50" height="50" />')

    profile_image.short_description = 'Profile Image'


    # @receiver(post_save, sender=User)
    # def create_user_profile(sender, instance, created, **kwargs):
    #     if created:
    #         Profile.objects.create(user=instance)

    # @receiver(post_save, sender=User)
    # def save_user_profile(sender, instance, **kwargs):
    #     instance.profile.save()


@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)