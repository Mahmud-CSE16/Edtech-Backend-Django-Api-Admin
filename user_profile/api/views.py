from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import authenticate

from rest_framework.decorators import api_view , permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token

from user_profile.models import Profile

from user_profile.api.serializers import UserSerializer, ProfileSerializer


# register
@api_view(['POST',])
def registration_api_view(request):
    if request.method == 'POST':
        serializer = UserSerializer(data = request.data)
        print(request.data)
        data={}
        if serializer.is_valid():
            user = serializer.save()

            profile_serializer = ProfileSerializer(user.profile)

            data['response'] = "Successfully registered"
            # profile
            data['profile'] = profile_serializer.data
            # auth token
            data['token'] = Token.objects.get(user=user).key
            #is registered

            date['isRegistered'] = True
        else:
            data = serializer.errors
            date['isRegistered'] = False

        return Response(data)


# login
class LoginAPIView(APIView):

    authentication_classes = []
    permission_classes = []

    def post(self, request):
        context={}

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)

        if user:
            try:
                token = Token.objects.get(user=user).key
                
            except Token.DoesNotExist:
                token = Token.objects.create(user=user).key
                
            
            
            context['response'] = 'Successfully authenticated.'
            context['profile'] = ProfileSerializer(user.profile).data
            context['token'] = token
            context['isLoggedIn'] = True
            
        else:
            context['response'] = 'Error'
            context['error message'] = 'Invalid credentials'
            context['isLoggedIn'] = False


        return Response(context)







# get profile
@api_view(['GET',])
@permission_classes([IsAuthenticated,])
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
@permission_classes([IsAuthenticated,])
def profile_api_update_view(request):
    try :
        profile = request.user.profile
    except Profile.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = ProfileSerializer(profile,data=request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data['response'] = "Account updata success"
            data['profile'] = serializer.data
            return Response(data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)