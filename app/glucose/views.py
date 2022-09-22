from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .models import Glucose
from .serializers import GlucoseSerializer
from authentication.models import User
from app.core import CheckUserToken


class GlucoseView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    
    def get(self, request, user_id):
        found_user = User.objects.filter(pk=user_id)

        if not found_user:
            return Response(status=status.HTTP_404_NOT_FOUND)

        check_credencials = CheckUserToken(request, user_id)

        if not check_credencials:
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
        
     
        serializer = GlucoseSerializer(glucose, many=True)

        return Response({'username': request.user.username, 'glucose_level':serializer.data}, status=status.HTTP_200_OK)


    def post(self, request):
        serializer = GlucoseSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


        found_user = User.objects.filter(id=request.data['user_id'])

        if not found_user:
            return Response(status=status.HTTP_404_NOT_FOUND)

        check_credencials = CheckUserToken(request, request.data['user_id'])

        if not check_credencials:
            return Response(status=status.HTTP_401_UNAUTHORIZED)

        glucose = Glucose.objects.create(**request.data) 

        serializer = GlucoseSerializer(glucose)

        return Response(serializer.data, status=status.HTTP_201_CREATED)