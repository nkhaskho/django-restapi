


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import generics

from django.http import Http404

from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Project, User
from .serlializers import ProjectSerializer
from rest_framework.response import Response
from .serlializers import UserSerializer


class UserList(generics.ListCreateAPIView):
    """
    List all users, or create a new user.
    """
    queryset = User.objects.filter(is_active=True)
    serializer_class = UserSerializer
    #permission_classes = (IsAuthenticated,)


class UserDetail(APIView):
    """
    Retrieve, update or delete a project identity.
    """
    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        user = self.get_object(pk)
        user.is_active = False
        user.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
        #return Response(status=status.HTTP_400_BAD_REQUEST)


class ProjectList(generics.ListCreateAPIView):
    """
    List all projects, or create a new project.
    """
    queryset = Project.objects.filter(deleted=False)
    serializer_class = ProjectSerializer
    #permission_classes = (IsAuthenticated,)


class ProjectDetail(APIView):
    """
    Retrieve, update or delete a project identity.
    """
    def get_object(self, pk):
        try:
            return Project.objects.get(pk=pk)
        except Project.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        project = self.get_object(pk)
        serializer = ProjectSerializer(project)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        project = self.get_object(pk)
        serializer = ProjectSerializer(project, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        project = self.get_object(pk)
        project.deleted = True
        project.save()
        return Response(status=status.HTTP_204_NO_CONTENT)

