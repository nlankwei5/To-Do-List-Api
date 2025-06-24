from rest_framework import serializers
from .models import *
from datetime import datetime


class ToDoSerializer(serializers.ModelSerializer):
    class Meta :
        model = ToDo
        fields = ('id', 'title', 'description', 'date', 'completed') 
    
    def validate_due_date(self, value):
        if value < datetime.today():
             raise serializers.ValidationError("Date cannot be in the past.")


    

class ToDoUserSerializer(serializers.ModelSerializer):
    class Meta :
        model = User
        fields = ('id', 'username', 'email', 'password')

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


