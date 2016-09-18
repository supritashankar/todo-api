from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from serializers import UserSerializer, TodoSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from models import Todo

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class TodoView(APIView):
    """
    API endpoint that allows todos to be viewed or edited
    """
    def get(self, request, format=None):
        todos = Todo.objects.all()
        serializer = TodoSerializer(todos, many=True, context={'request': request})
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TodoDetailView(APIView):

    def get(self, request, todo_id):
        print 'HERE', todo_id
        try:
            todo = Todo.objects.get(id=todo_id)
        except:
            return HttpResponse(status=404)
        serializer = TodoSerializer(todo, context={'request': request})
        return Response(serializer.data)

    def delete(self, request, todo_id):
        print todo_id
        try:
            todo = Todo.objects.get(id=todo_id)
        except:
            return HttpResponse(status=404)
        todo.delete()
        return HttpResponse(status=204)


def index(request):
    return HttpResponse("Hello world!!")
