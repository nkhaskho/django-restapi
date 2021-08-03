from .models import Project, User
from rest_framework import serializers


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'identifier', 'role', 'project', 'is_active', 'is_staff',)
    
    def create(self, validated_data):
        user = User(email=validated_data['email'], username=validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()
        return user