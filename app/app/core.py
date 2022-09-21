from rest_framework.authtoken.models import Token
    

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