from rest_framework import serializers

from user_profile.models import Profile, District, NotificationStatus
from django.contrib.auth.models import User
from common.api.serializers import CategorySerializer, SubCategorySerializer


class DistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model = District
        fields = "__all__"



#ProfileSerializer
class ProfileSerializer(serializers.ModelSerializer):
    level = CategorySerializer(read_only=True,)
    sub_level = SubCategorySerializer(read_only=True,)
    district = DistrictSerializer(read_only=True,)

    class Meta:
        model = Profile
        fields = ['uid','name','email','profile_pic_url','phone','address','dateOfBirth','institute','level','sub_level','district',]


class ProfileSerializerForRegistration(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['uid','name','email','profile_pic_url','phone','address','dateOfBirth','institute','level','sub_level','district',]


class NotificationStatusSerializer(serializers.ModelSerializer):
    last_seen = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", required=False)
    class Meta:
        model = NotificationStatus
        fields = ['device_token','last_seen',]

#UserSerializer
class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    profile = ProfileSerializerForRegistration()
    notification_status = NotificationStatusSerializer()

    class Meta:
        model = User
        fields = ['username','password','profile','notification_status']
        
    def create(self, validated_data, instance=None):
        profile_data = validated_data.pop('profile')
        notification_status_data = validated_data.pop('notification_status')
        user = User.objects.create(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        Profile.objects.update_or_create(user=user,**profile_data)
        NotificationStatus.objects.update_or_create(user=user,**notification_status_data)
        return user
        
    