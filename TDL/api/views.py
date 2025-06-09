from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import AllowAny
from .serializers import *
from .models import *


# Create your views here.

class ListToDo(generics.ListAPIView):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer

class UpdateToDo(generics.RetrieveUpdateAPIView):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer

class CreateToDo(generics.CreateAPIView):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer


class DeleteToDo(generics.DestroyAPIView):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer

class UserRegistration(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = ToDoUserSerializer
    permission_classes = [AllowAny]