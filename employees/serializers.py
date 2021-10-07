from .models import Project, User
from rest_framework import serializers


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'registration_number', 
                'role', 'project', 'created_at', 'is_active', 'is_staff',)
        #fields = ('id', 'email', 'first_name', 'last_name' ,'security_question', 'security_question_answer', 'password', 'is_active', 'is_staff')
        #read_only_fields = ('password',)
        """
        extra_kwargs = {
            'password': {'read_only': True}
        }
        """
    
    def create(self, validated_data):
        user = User(email=validated_data['email'], username=validated_data['username'])
        user.set_password(validated_data['password'])
        user.project = validated_data['project']
        user.registration_number = validated_data['registration_number']
        user.save()
        return user