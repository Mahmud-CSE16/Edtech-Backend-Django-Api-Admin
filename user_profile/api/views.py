from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from django.contrib.auth import authenticate

from rest_framework.decorators import api_view , permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from mathbyrony.api_permissons import Check_API_KEY_Auth

from user_profile.models import Profile, NotificationStatus

from user_profile.api.serializers import UserSerializer, ProfileSerializer, ProfileSerializerForRegistration, NotificationStatusSerializer
import json


# register
@api_view(['POST',])
@permission_classes([Check_API_KEY_Auth,])
@authentication_classes([])
def registration_api_view(request):
    if request.method == 'POST':
        serializer = UserSerializer(data = request.data)
        # print(request.data)
        data={}
        if serializer.is_valid():
            user = serializer.save()

            profile_serializer = ProfileSerializer(user.profile)
            notification_status_serializer = NotificationStatusSerializer(user.notificationstatus)

            data['response'] = "Successfully registered"
            # profile
            data['profile'] = profile_serializer.data
            # notification status
            data['notification_status'] = notification_status_serializer.data
            # auth token
            data['token'] = Token.objects.get(user=user).key
            #is registered

            data['isRegistered'] = True
        else:
            data = serializer.errors
            data['isRegistered'] = False

        return Response(data)


# login
class LoginAPIView(APIView):

    authentication_classes = []
    permission_classes = [Check_API_KEY_Auth,]

    def post(self, request):
        context={}

        username = request.data['username']
        password = request.data['password']

        user = authenticate(username=username,password=password)
        print(user.notificationstatus)

        if user:
            try:
                token = Token.objects.get(user=user).key
                
            except Token.DoesNotExist:
                token = Token.objects.create(user=user).key
                
            
            context['response'] = 'Successfully authenticated.'
            context['profile'] = ProfileSerializer(user.profile).data
            context['notification_status'] = NotificationStatusSerializer(user.notificationstatus).data
            context['token'] = token
            context['isLoggedIn'] = True
            
        else:
            context['response'] = 'Error'
            context['error message'] = 'Invalid credentials'
            context['isLoggedIn'] = False


        return Response(context)







# get profile
@api_view(['GET',])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated & Check_API_KEY_Auth ])
def profile_api_view(request):
    try :
        profile = request.user.profile
    except Profile.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ProfileSerializer(profile)
        return Response(serializer.data)


# update profile
@api_view(['PUT',])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated & Check_API_KEY_Auth ])
def profile_api_update_view(request):
    try :
        profile = request.user.profile
    except Profile.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = ProfileSerializerForRegistration(profile,data=request.data)
        data = {}
        if serializer.is_valid():
            profile = serializer.save()
            data['response'] = "Account update success"
            data['profile'] = ProfileSerializer(profile).data
            return Response(data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# get notification status
@api_view(['GET',])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated & Check_API_KEY_Auth ])
def notification_status_api_view(request):
    try :
        notificationstatus = request.user.notificationstatus
    except NotificationStatus.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = NotificationStatusSerializer(notificationstatus)
        return Response(serializer.data)


# update notification status
@api_view(['PUT',])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated & Check_API_KEY_Auth ])
def notification_status_api_update_view(request):
    try :
        notificationstatus = request.user.notificationstatus
    except NotificationStatus.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = NotificationStatusSerializer(notificationstatus,data=request.data)
        data = {}
        if serializer.is_valid():
            notificationstatus = serializer.save()
            data['response'] = "update success"
            data['notificationstatus'] = NotificationStatusSerializer(notificationstatus).data
            return Response(data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



""" class DistrictListAPIView(ListAPIView):
    queryset = District.objects.all().order_by('name')
    serializer_class = DistrictSerializer
    authentication_classes = []
    permission_classes = [Check_API_KEY_Auth,] """