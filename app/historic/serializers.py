from rest_framework import serializers


class HistoricSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    historic = serializers.CharField()
    medicines = serializers.CharField(required=False)
    surgeries = serializers.CharField(required=False)
    user_id = serializers.IntegerField()