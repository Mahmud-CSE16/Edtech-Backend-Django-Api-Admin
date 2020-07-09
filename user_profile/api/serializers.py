from rest_framework import serializers

from user_profile.models import Profile, District
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
        fields = ['uid','device_token','name','email','profile_pic_url','phone','address','dateOfBirth','institute','level','sub_level','district',]


#UserSerializer
class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    profile = ProfileSerializer()

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
        
    