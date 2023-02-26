from rest_framework import serializers
from .models import students
class studentsserializer(serializers.Serializer): 
    name=serializers.CharField(max_length=100)
    roll=serializers.IntegerField()
    city=serializers.CharField(max_length=100)
    def create(self, validated_data):
      return students.objects.create(**validated_data)
