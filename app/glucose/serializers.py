from rest_framework import serializers
from authentication.models import User

class GlucoseSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    glucose = serializers.IntegerField()
    date_time = serializers.DateTimeField(read_only=True)
    user_id = serializers.IntegerField()
