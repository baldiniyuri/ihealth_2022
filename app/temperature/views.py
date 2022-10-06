from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .models import Temperature
from .serializers import TemperatureSerializer
from authentication.models import User
from app.core import CheckUserToken, FindUser, CheckAdminOrMedicCredentials


class TemperatureView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Temperature.objects.all()


    def get(self, request, user_id):

        if not FindUser(user_id):
            return Response(status=status.HTTP_404_NOT_FOUND)


        if not CheckUserToken(request, user_id):
            return Response(status=status.HTTP_401_UNAUTHORIZED)

        min = self.request.query_params.get('min', '')
        max = self.request.query_params.get('max', '')

        if min and max:

            param = "date_time"

            lookup_filter = {}
            lookup_filter[f'{param}__gte'] = min
            lookup_filter[f'{param}__lte'] = max
            temperature = self.queryset.filter(**lookup_filter, user_id=user_id)
        else:
            temperature = self.queryset.filter(user=user_id)
        
        temperature = self.queryset.filter(user=user_id)
     
        serializer = TemperatureSerializer(temperature, many=True)

        return Response({'username': request.user.username, 'temperature_level':serializer.data}, status=status.HTTP_200_OK)


    def post(self, request):
        serializer = TemperatureSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


        if not FindUser(request.data['user_id']):
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

        user = User.objects.get(id=request.data['user_id'])  

        temperature = self.queryset.create(user=user, **request.data) 

        serializer = TemperatureSerializer(temperature)

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class TemepratureMedicView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Temperature.objects.all()
    
    def get(self, request, user_id, medic_id):

        if not FindUser(user_id) or not FindUser(medic_id):
            return Response(status=status.HTTP_404_NOT_FOUND)

        if not CheckAdminOrMedicCredentials(request, medic_id):
            return Response(status=status.HTTP_401_UNAUTHORIZED)

        min = self.request.query_params.get('min', '')
        max = self.request.query_params.get('max', '')
 
        if min and max:

            param = "date_time"

            lookup_filter = {}
            lookup_filter[f'{param}__gte'] = min
            lookup_filter[f'{param}__lte'] = max
            
            temeprature = self.queryset.filter(**lookup_filter, user=user_id)
        else:
            temeprature = self.queryset.filter(user=user_id)
        
        user = User.objects.get(id=user_id)
        full_name = '{} {}'.format(user.first_name, user.last_name)

        serializer = TemperatureSerializer(temeprature, many=True)

        return Response({'user': full_name, 'temperature_level':serializer.data}, status=status.HTTP_200_OK)