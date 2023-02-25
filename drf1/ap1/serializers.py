from rest_framework import serializers

class studentsserializer(serializers.Serializer):
    name=serializers.CharField(max_length=100)
    roll=serializers.IntegerField()
    cp=serializers.CharField(max_length=100)
