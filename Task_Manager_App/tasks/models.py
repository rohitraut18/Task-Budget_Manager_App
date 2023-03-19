from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class TaskCategory(models.Model):
    category = models.CharField(max_length=128)
    def __str__(self):
        return self.category

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=400)
    category = models.ForeignKey(TaskCategory, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)