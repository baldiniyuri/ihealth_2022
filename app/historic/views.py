from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .models import Historic
from .serializers import HistoricSerializer
from authentication.models import User
from app.core import CheckUserToken, FindUser, CheckAdminOrMedicCredentials


class HistoricView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Historic.objects.all()


    def get(self, request, user_id):

        if not FindUser(user_id):
            return Response(status=status.HTTP_404_NOT_FOUND)


        if not CheckUserToken(request, user_id):
            return Response(status=status.HTTP_401_UNAUTHORIZED)

        historic = self.queryset.objects.filter(user=user_id)
     
        serializer = HistoricSerializer(historic, many=True)

        return Response({'username': request.user.username, 'Historic':serializer.data}, status=status.HTTP_200_OK)


    def post(self, request, user_id):
        serializer = HistoricSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        found_user = User.objects.filter(id=user_id)

        if not found_user:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

        user = User.objects.get(id=user_id)  
        
        historic = self.queryset.create(user=user, **request.data) 

        serializer = HistoricSerializer(historic)

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class HistoricMedicView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Historic.objects.all()
    
    def get(self, request, user_id, medic_id):

        if not FindUser(user_id) or not FindUser(medic_id):
            return Response(status=status.HTTP_404_NOT_FOUND)

        if not CheckAdminOrMedicCredentials(request, medic_id):
            return Response(status=status.HTTP_401_UNAUTHORIZED)

        historic = self.queryset.filter(user=user_id)
        
        user = User.objects.get(id=user_id)
        full_name = '{} {}'.format(user.first_name, user.last_name)

        serializer = HistoricSerializer(historic)

        return Response({'user': full_name, 'historic':serializer.data}, status=status.HTTP_200_OK)