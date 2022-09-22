from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from defense.models import Defense
from defense.serializers import DefenseSerializers
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from authentication.models import User
from app.core import CheckUserToken


class DefenseViewAdminView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]


    def get(self, request):

        blacklist = Defense.objects.all()

        serializer = DefenseSerializers(blacklist, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK) 
    

    def delete(self, request, attack_ip, admin_id):
        found_user = User.objects.filter(id=admin_id)

        found_attack = Defense.objects.filter(ip=attack_ip)

        if not found_attack or not found_user:
            return Response(status=status.HTTP_404_NOT_FOUND)

        user = User.objects.get(id=admin_id)
   
        check_credencials = CheckUserToken(request, admin_id)

        if check_credencials and user.is_superuser:

            Defense.objects.filter(ip=attack_ip).all().delete()
            
            return Response(status=status.HTTP_204_NO_CONTENT)
        
        return Response(status=status.HTTP_401_UNAUTHORIZED)