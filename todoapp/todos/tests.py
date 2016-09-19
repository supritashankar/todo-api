# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework.test import force_authenticate
from .views import TodoView, TodoDetailView
from .models import Todo

class SimpleTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.staffuser = User.objects.create_user(username='supushank', email='supu@…', password='123')
        self.user = User.objects.create_superuser(username='sups', email='sups@…', password='1234')
        self.user.save()


    def test_todos_with_new_user(self):
        self.client.login(username='supushank', password='123')
        response = self.client.get('/todos/')
        self.assertEqual(response.status_code, 403) #Returns 403 as the user is not superuser

    def test_user_with_anonymous_user(self):
        response = self.client.get('/todos/')
        self.assertEqual(response.status_code, 401) #Returns 401 as it as unauthorized request

    def test_todos_get(self):
        user = User.objects.get(username='sups')
        self.client.force_authenticate(user=user)
        response = self.client.get('/todos/')
        self.assertEqual(response.status_code, 200)

    def test_todos_post(self):
        user = User.objects.get(username='sups')
        self.client.force_authenticate(user=user)
        response = self.client.post('/todos/', {'todo_text': 'take a nap', 'completed': 'false'}, format='json')
        self.assertEqual(response.status_code, 201)


    def test_todos_put_404(self):
        user = User.objects.get(username='sups')
        self.client.force_authenticate(user=user)
        response = self.client.put('/todos/1/', {'todo_text': 'take a nap', 'completed': 'true'}, format='json')
        self.assertEqual(response.status_code, 404)

    def test_todos_put(self):
        user = User.objects.get(username='sups')
        self.client.force_authenticate(user=user)
        Todo.objects.create(todo_text="take a nap",completed="false")
        response = self.client.put('/todos/1/', {'todo_text': 'take a nap', 'completed': 'true'}, format='json')
        self.assertEqual(response.status_code, 200)

    def test_todos_delete_404(self):
        user = User.objects.get(username='sups')
        self.client.force_authenticate(user=user)
        response = self.client.delete('/todos/1/')
        self.assertEqual(response.status_code, 404)

    def test_todos_delete(self):
        user = User.objects.get(username='sups')
        self.client.force_authenticate(user=user)
        Todo.objects.create(todo_text="take a nap",completed="false")
        response = self.client.delete('/todos/1/')
        self.assertEqual(response.status_code, 204)
