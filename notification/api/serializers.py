from rest_framework import serializers
from notification.models import Notification
from common.api.serializers import CategorySerializer


class NotificationSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=True,)
    published_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", required=False)


    class Meta:
        model = Notification
        fields = ['title','short_description','long_description','categories','published_time',]
