from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .models import Glucose
from .serializers import GlucoseSerializer
from authentication.models import User
from app.core import CheckUserToken, FindUser, CheckAdminOrMedicCredentials


class GlucoseView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    
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
            glucose = Glucose.objects.filter(**lookup_filter, user=user_id)
        else:
            glucose = Glucose.objects.filter(user=user_id)
        
        user = User.objects.get(id=user_id)
        full_name = '{} {}'.format(user.first_name, user.last_name)

        serializer = GlucoseSerializer(glucose, many=True)

        return Response({'user': full_name, 'glucose_level':serializer.data}, status=status.HTTP_200_OK)


    def post(self, request):
        serializer = GlucoseSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


        found_user = User.objects.filter(id=request.data['user_id'])

        if not found_user:
            return Response(status=status.HTTP_404_NOT_FOUND)


        if not CheckUserToken(request, request.data['user_id']):
            return Response(status=status.HTTP_401_UNAUTHORIZED)

        glucose = Glucose.objects.create(**request.data) 

        serializer = GlucoseSerializer(glucose)

        return Response(serializer.data, status=status.HTTP_201_CREATED)



class GlucoseMedicView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    
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
            
            glucose = Glucose.objects.filter(**lookup_filter, user=user_id)
        else:
            glucose = Glucose.objects.filter(user=user_id)
        
        user = User.objects.get(id=user_id)
        full_name = '{} {}'.format(user.first_name, user.last_name)

        serializer = GlucoseSerializer(glucose, many=True)

        return Response({'user': full_name, 'glucose_level':serializer.data}, status=status.HTTP_200_OK)