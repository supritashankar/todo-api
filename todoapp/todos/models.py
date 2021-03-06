import django
from django.db import models
from django.utils import timezone


class Todo(models.Model):
    todo_text = models.CharField(max_length=200)
    completed = models.BooleanField()
    created_date = models.DateTimeField(default=django.utils.timezone.now)

    def __str__(self):
        return self.todo_text
