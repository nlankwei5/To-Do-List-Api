from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from .serializers import *
from .models import *



# Create your views here.

class ListToDo(generics.ListAPIView):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['completed']
    search_fields = ['title']
    ordering_fields = ['date']



    def get_queryset(self):
        return ToDo.objects.filter(user=self.request.user)

class UpdateToDo(generics.RetrieveUpdateAPIView):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter,filters.OrderingFilter]
    filterset_fields = ['completed']
    search_fields = ['title']
    ordering_fields = ['date']


    def get_queryset(self):
        return ToDo.objects.filter(user=self.request.user)

class CreateToDo(generics.CreateAPIView):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]


    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        raise 


class DeleteToDo(generics.DestroyAPIView):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    

    def get_queryset(self):
        return ToDo.objects.filter(user=self.request.user)

class UserRegistration(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = ToDoUserSerializer
    permission_classes = [AllowAny]
