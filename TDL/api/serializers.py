from rest_framework import serializers
from .models import *

class ToDoSerializer(serializers.ModelSerializer):
    class Meta :
        model = ToDo
        fields = ('id', 'title', 'description', 'date', 'completed') 

class ToDoUserSerializer(serializers.ModelSerializer):
    class Meta :
        model = User
        fields = ('id', 'username', 'email', 'password')

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


