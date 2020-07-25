from rest_framework import serializers
from notification.models import Notification
from common.api.serializers import SubCategorySerializer


class NotificationSerializer(serializers.ModelSerializer):
    subcategories = SubCategorySerializer(many=True,)
    published_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", required=False)


    class Meta:
        model = Notification
        fields = ['title','short_description','long_description','subcategories','published_time',]
