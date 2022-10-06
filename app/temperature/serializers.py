from rest_framework import serializers


class TemperatureSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    temperature = serializers.FloatField()
    date_time = serializers.DateTimeField(read_only=True) 
    user_id = serializers.IntegerField()