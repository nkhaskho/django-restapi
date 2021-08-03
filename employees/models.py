from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, AbstractUser, BaseUserManager, PermissionsMixin
from django.contrib.auth.hashers import make_password


USER_ROLE_CHOICES = [
    ('MANAGER', 'Manager'),
    ('LEADER', 'Leader'),
    ('USER', 'User')
]


class Project(models.Model):
    name = models.CharField(max_length=255)
    deleted = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.name


class UserManager(BaseUserManager):

    def create_user(self, username, email, password=None):
        if username is None:
            raise TypeError("username field is required")
        if email is None:
            raise TypeError("email field is required")
        if password is None:
            raise TypeError("password field is required")
        user = self.create_user(username=username, email=self.normalize_email(email), password=password)
        user.set_password(password)
        user.is_staff = True
        user.save()
        return user

    def create_superuser(self, username, email, password=None):
        if username is None:
            raise TypeError("username field is required")
        if email is None:
            raise TypeError("password should not be none")
        user = self.create_user(username, email, password)
        user.is_superuser = True
        user.is_staff = True
        user.role = 'MANAGER'
        user.save()
        return user


class User(AbstractUser, PermissionsMixin):
    username = models.CharField(max_length=255, unique=True, db_index=True)
    email = models.EmailField(unique=True)
    identifier = models.IntegerField(null=True)
    role = models.CharField(choices=USER_ROLE_CHOICES, max_length=20, default='USER')
    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'password']

    objects = UserManager()

    def __str__(self) -> str:
        return f'{self.username} ({self.email})'

    def tokens(self):
        return ''


