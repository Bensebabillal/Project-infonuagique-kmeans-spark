from rest_framework import serializers


class ItemSerializer(serializers.ModelSerializer):
    long = serializers.CharField(max_length=200)
    lat = serializers.FloatField()
    date_start = serializers.IntegerField(required=False, default=1)
    date_end = serializers.IntegerField(required=False, default=1)
