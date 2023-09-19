from rest_framework import serializers
from .models import *

class SER_CR_Persons(serializers.ModelSerializer):
    class Meta:
        model = Persons
        fields = ('iin','name','age')
    
    def validate(self, attrs):
        if not attrs['iin'] or not attrs['name']:
            raise serializers.ValidationError("Нет нужных данных")
        else:
            return super().validate(attrs)

class SER_RUD_Persons(serializers.ModelSerializer):
    class Meta:
        model = Persons
        fields = ('iin','name','age')
        read_only_fields = ('iin','age')
    
    def validate(self, attrs):
        if not attrs['name']:
            raise serializers.ValidationError("Нет имени данных")
        else:
            return super().validate(attrs)