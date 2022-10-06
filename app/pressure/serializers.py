from rest_framework import serializers


class BloodPressueSerializers(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    systolic_level = serializers.IntegerField()
    diastolic_level = serializers.IntegerField()
    bpm = serializers.IntegerField()
    date_time = serializers.DateTimeField(read_only=True)
    user_id = serializers.IntegerField()