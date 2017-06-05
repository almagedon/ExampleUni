from django.contrib.auth.models import User
from rest_framework import serializers
from notes.models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username','password', 'email', 'is_staff', 'first_name', 'last_name')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


class NotesSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Notes
        fields = '__all__'