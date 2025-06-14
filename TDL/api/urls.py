from django.urls import path 
from .views import *



urlpatterns = [
    path('<int:pk>/', UpdateToDo.as_view()),
    path('', ListToDo.as_view()),
    path('create/', CreateToDo.as_view()),
    path('delete/<int:pk>/', DeleteToDo.as_view()),
    path('register/', UserRegistration.as_view(), name='user-register'),
]
