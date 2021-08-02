from django.db import models
from django.contrib.auth.models import AbstractUser

USER_ROLE_CHOICES = [
    ('MANAGER', 'Manager'),
    ('LEADER', 'Leader'),
    ('USER', 'User')
]

# Create your models here.
class Employee(models.Model):
    username = models.CharField(max_length=255)
    email = models.EmailField()
    password = models.CharField(max_length=255)
    identifier = models.IntegerField(null=True)
    role = models.CharField(choices=USER_ROLE_CHOICES, max_length=20, default='USER')
    deleted = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.username