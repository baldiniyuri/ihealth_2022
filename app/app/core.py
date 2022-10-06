from rest_framework.authtoken.models import Token
from authentication.models import User 


def CheckUserToken(request, user_id):
    user_id_token = Token.objects.get(user=user_id)
        
    request_token = request.auth.key
        
    if user_id_token.key == request_token:
        return True
        
    return False


def DeleteUserToken(user_id):
    token_to_delete = Token.objects.get(user=user_id)
   
    if token_to_delete:
        token_to_delete.delete()
        return True

    return False


def CheckAdmin(user_id):
    user = User.objects.get(id=user_id)
    if user.is_superuser:
        return True
    return False


def CheckMedic(user_id):
    user = User.objects.get(id=user_id)

    if user.is_medic:
        return True
    return False


def FindUser(user_id):
    found = User.objects.filter(id=user_id)
    if found:
        return True
    return False


def CheckAdminCredentials(request, user_id):
    if CheckUserToken(request, user_id) and CheckAdmin(user_id):
        return True
    return False


def CheckAdminOrMedicCredentials(request, user_id):
    if CheckUserToken(request, user_id) and CheckAdmin(user_id) or CheckMedic(user_id):
        return True
    return False
