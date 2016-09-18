from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from serializers import UserSerializer, TodoSerializer
from models import Todo

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class TodoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows todos to be viewed or edited
    """
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


def index(request):
    return HttpResponse("Hello world!!")
