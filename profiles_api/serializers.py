from rest_framework import serializers


class HelloSerializer(serializers.Serializer):
    """Serial for field na,e hellow apis"""
    name = serializers.CharField(max_length=10)