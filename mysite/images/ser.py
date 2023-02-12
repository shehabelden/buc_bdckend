from rest_framework import serializers
from .models import *
class images_ser_post(serializers.ModelSerializer):
    class Meta:
     model=images_model
     fields=['image']
     def create(self, validated_data):
         return images_model.objects.create(**validated_data)
class images_ser_get(serializers.ModelSerializer):
    class Meta:
     model=images_model
     fields=['image']
     def create(self, validated_data):
         return images_model.objects.create(**validated_data)
