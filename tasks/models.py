#creating models for Task management appliction

from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    Title=models.CharField(max_length=256)
    description=models.TextField(blank=True)
    is_completed=models.BooleanField(False)
    created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Title

