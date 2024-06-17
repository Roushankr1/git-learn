from rest_framework import serializers


class characterserializer(serializers.Serializer):
    character_name = serializers.CharField(max_length=20)
    character_price = serializers.IntegerField()
    character_quantity = serializers.IntegerField()
    character_date = serializers.DateField()
