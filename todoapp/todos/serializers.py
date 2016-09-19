from django.contrib.auth.models import User
from rest_framework import serializers
from models import Todo

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')

class TodoSerializer(serializers.ModelSerializer):
    def validate_todo_text(self, value):
        # todo should consist of at least 2 or more words.
        if not len(value.split()) > 1:
            raise serializers.ValidationError("Todo task should have at least 2 words")
        return value
    class Meta:
        model = Todo
        fields = ('todo_text', 'completed')
