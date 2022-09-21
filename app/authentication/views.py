from .models import  User
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework.response import Response
from .serializers import UserSerializer


class UsersView(APIView):
    def post(self, request):

        serializer = UserSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        find_user_by_email = User.objects.filter(email=request.data['email']).exists()

        if find_user_by_email:
            return Response(serializer.data, status=status.HTTP_409_CONFLICT)
        
        user = User.objects.create_user(username=request.data['email'],is_staff=False, is_superuser=False,**request.data)

        token = Token.objects.get_or_create(user=user)[0]
      
        serializer = UserSerializer(user)

        return Response({"data": serializer.data, "token":token.key}, status=status.HTTP_201_CREATED)

