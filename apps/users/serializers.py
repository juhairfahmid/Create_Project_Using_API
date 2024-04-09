from rest_framework import serializers
from django.contrib.auth.models import User

class RegistrationSerializer(serializers.Serializer):

    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, munni):
        
        user = User.objects.filter(username = munni['username'])
        if user: 
            raise serializers.ValidationError("username is taken")
        
        return munni
    
    def create(self, validated_data):
        user = User.objects.create(username = validated_data['username'])
        user.set_password(validated_data['password'])

        return validated_data
