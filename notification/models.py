from django.db import models
from common.models import SubCategory
from datetime import datetime
from pyfcm import FCMNotification
from django.conf import settings
from ckeditor_uploader.fields import RichTextUploadingField
from django.db.models.signals import m2m_changed


# Create your models here.

class Notification(models.Model):
    subCategories = models.ManyToManyField(SubCategory)
    title = models.CharField(max_length=255)
    short_description = models.TextField()
    # long_description = models.TextField(blank=True, null=True)
    long_description = RichTextUploadingField(blank=True, null=True)
    created_time = models.DateTimeField(default = datetime.now)
    published_time = models.DateTimeField(blank=True, null=True)
    published = models.BooleanField(default = False)

    class Meta:
        ordering = ('-created_time',)

    def save(self, *args, **kwargs):

        print(self.published)
        #save
        super(Notification, self).save(*args, **kwargs)

        if(self.published == True):
            self.published_time = datetime.now()
            
            push_service = FCMNotification(api_key=settings.FCM_SERVER_KEY)

            # Conditional topic messaging
            #topic_condition = ""

            print(self.subCategories.all())

            for category in self.subCategories.all():
                #topic_condition += "'{}' in topics || ".format(category.name)

                data_message = {
                    "click_action": 'FLUTTER_NOTIFICATION_CLICK',
                    "title": self.title,
                    "short_description": self.short_description,
                    "long_description": self.long_description,
                    # "image_url": event.image_url
                }

                result = push_service.notify_topic_subscribers(
                    topic_name="all", #category.name
                    #condition = topic_condition,
                    message_title=self.title, 
                    message_body=self.short_description,
                    click_action = 'FLUTTER_NOTIFICATION_CLICK',
                    data_message = data_message
                )
                

            """ topic_condition += "'all' in topics"

            print(topic_condition)


            data_message = {
                "click_action": 'FLUTTER_NOTIFICATION_CLICK',
                "title": self.title,
                "short_description": self.short_description,
                "long_description": self.long_description,
                # "image_url": event.image_url
            }

            result = push_service.notify_topic_subscribers(
                # topic_name="all",
                condition = topic_condition,
                message_title=self.title, 
                message_body=self.short_description,
                click_action = 'FLUTTER_NOTIFICATION_CLICK',
                data_message = data_message
            )
            print(result) """



            # headers = {
            #     'Content-Type' : 'application/json',
            #     'Authorization' : 'key=AAAA9lV8u74:APA91bE-L_tirOl2DP0N9THg6_e3wbGGUa6xHSRGoC9-h9oU44pJrJMQ2MpguhQ-y2UVMKtyoV89oxU0J5bQ5LqYfLSNegYydkeAGB2n-nnIQtmafWSwTYX1gf8HyX8wKds5HZIPMYvq'
            # }

            # data = {
            #     "notification": {"body": "this is a body1","title": "this is a title1"}, 
            #     "priority": "high",
            #     "data": {"click_action": "FLUTTER_NOTIFICATION_CLICK", "id": "1", "status": "done","body": "this is a body","title": "this is a title"}, 
            #     "to": "/topics/all"
            # }

            # content = requests.post('https://fcm.googleapis.com/fcm/send',headers = headers, data = data)
            # print(content)
        else:
            self.published_time = None 

        #save
        super(Notification, self).save(*args, **kwargs)

    def __str__(self):
        return self.title



""" after SubCategory added """
def subCategories_changed(sender, instance, action, reverse, *args, **kwargs):

    print("inside subCategories_changed")
    if(instance.published == True):
            
        push_service = FCMNotification(api_key=settings.FCM_SERVER_KEY)

        # Conditional topic messaging
        #topic_condition = ""

        print(instance.subCategories.all())

        for category in instance.subCategories.all():
            #topic_condition += "'{}' in topics || ".format(category.name)

            data_message = {
                "click_action": 'FLUTTER_NOTIFICATION_CLICK',
                "title": instance.title,
                "short_description": instance.short_description,
                "long_description": instance.long_description,
                # "image_url": event.image_url
            }

            result = push_service.notify_topic_subscribers(
                topic_name="all", #category.name
                #condition = topic_condition,
                message_title=instance.title, 
                message_body=instance.short_description,
                click_action = 'FLUTTER_NOTIFICATION_CLICK',
                data_message = data_message
            )
           
    pass

m2m_changed.connect(subCategories_changed, sender=Notification.subCategories.through)