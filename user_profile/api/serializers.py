from rest_framework import serializers

from user_profile.models import Profile
from django.contrib.auth.models import User


# UserProfileSerializer
class UserProfileSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Profile
        fields = ['uid','device_token','name','email','profile_pic_url','phone','address','institute','level','district',]

#UserSerializer
class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    profile = UserProfileSerializer()

    class Meta:
        model = User
        fields = ['username','password','profile',]
        
    def create(self, validated_data, instance=None):
        profile_data = validated_data.pop('profile')
        user = User.objects.create(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        Profile.objects.update_or_create(user=user,**profile_data)
        return user
        

#ProfileSerializer
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['uid','device_token','name','email','profile_pic_url','phone','address','institute','level','sub_level','district',]

    