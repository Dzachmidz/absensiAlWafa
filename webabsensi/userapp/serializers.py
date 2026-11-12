from rest_framework import serializers


class RfidScanSerializer(serializers.Serializer):
    uid = serializers.CharField(max_length=50)
