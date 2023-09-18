from rest_framework import serializers
from .models import *

class SER_CR_Persons(serializers.ModelSerializer):
    class Meta:
        model = Persons
        fields = '__all__'
    
    def validate(self, attrs):
        if not attrs['iin'] or not attrs['name'] or not attrs['age']:
            raise serializers.ValidationError("Нет нужных данных")
        else:
            return super().validate(attrs)

class SER_RUD_Persons(serializers.ModelSerializer):
    class Meta:
        model = Persons
        fields ='__all__'
        read_only_fields = ('iin','age')
    
    def validate(self, attrs):
        if not attrs['name']:
            raise serializers.ValidationError("Нет имени данных")
        else:
            return super().validate(attrs)