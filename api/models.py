from django.db import models
from django.contrib.auth.models import AbstractUser

class User(models.Model):
    username = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    group = models.ForeignKey('Group',on_delete=models.SET_NULL,null=True)
    def __str__(self):
        return self.username
class Group(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    def __str__(self):
        return self.name
