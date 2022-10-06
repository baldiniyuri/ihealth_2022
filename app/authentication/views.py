from .models import  User
from .serializers import UserSerializer, CredentialSerializer, ProfilePictureSerializers
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from app.core import DeleteUserToken
from defense.blacklist import Blacklist
from django.contrib.auth import authenticate


class UsersView(APIView):
    def post(self, request):

        serializer = UserSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        find_user_by_email = User.objects.filter(email=request.data['email']).exists()

        if find_user_by_email:
            return Response(serializer.data, status=status.HTTP_409_CONFLICT)
        
        user = User.objects.create_user(username=request.data['email'],**request.data)

        token = Token.objects.get_or_create(user=user)[0]
      
        serializer = UserSerializer(user)

        return Response({"data": serializer.data, "token":token.key}, status=status.HTTP_201_CREATED)


class LoginView(APIView):
    def post(self, request):

        if Blacklist(request):
            return Response(status=status.HTTP_403_FORBIDDEN)

        serializer = CredentialSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        user = authenticate(username=request.data['email'], password=request.data['password'])

        if user is not None:
            token = Token.objects.get_or_create(user=user)[0]
            return Response({'token': token.key, "user_id": user.id, "is_staff": user.is_staff, "is_superuser": user.is_superuser})

        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)


class Logout(APIView):
    def post(self, request, user_id):
        found_user = User.objects.get(id=user_id)

        if found_user:
            DeleteUserToken(user_id)
            return Response(status=status.HTTP_200_OK)
             
        return Response(status=status.HTTP_404_NOT_FOUND)


class ProfilePictureView(APIView):

    parser_classes = [MultiPartParser, FormParser, JSONParser]
    
    def put(self, request, *args, **kwargs):

        if Blacklist(request):
            return Response(status=status.HTTP_403_FORBIDDEN)
     
        try:
            found_user = User.objects.filter(pk=request.data['user_id'])
  
            if not found_user:
                    return Response(status=status.HTTP_404_NOT_FOUND)

            picture = User.objects.get(pk=request.data['user_id'])
            picture.image = request.data['image']
            picture.save()

            return Response( status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
    

    def get(self, request, user_id):

        if Blacklist(request):
            return Response(status=status.HTTP_403_FORBIDDEN)

        found_user = User.objects.filter(pk=user_id)

        if not found_user:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        user = User.objects.get(pk=user_id)

        serializers = ProfilePictureSerializers(user)

        return Response(serializers.data, status=status.HTTP_200_OK)
