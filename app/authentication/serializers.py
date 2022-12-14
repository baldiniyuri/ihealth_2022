from rest_framework import serializers


class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    password = serializers.CharField(write_only=True)
    city = serializers.CharField()
    uf = serializers.CharField()
    country = serializers.CharField()
    image = serializers.ImageField(required=False)
    email = serializers.EmailField()
    is_pacient = serializers.BooleanField()
    is_medic = serializers.BooleanField()
    is_superuser = serializers.BooleanField(required=False)


class CredentialSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
    

class ProfilePictureSerializers(serializers.Serializer):
    user_id = serializers.IntegerField(read_only=True)
    image = serializers.ImageField()