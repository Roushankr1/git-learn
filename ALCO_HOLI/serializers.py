from rest_framework import serializers


class instrumentserializer(serializers.Serializer):
    instrument_name = serializers.CharField(max_length=20)
    instrument_prize = serializers.IntegerField()
    instrument_quantity = serializers.IntegerField()
    instrument_date = serializers.DateField()
