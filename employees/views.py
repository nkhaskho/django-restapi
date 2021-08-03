


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import generics

from django.http import Http404

from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Employee, Project
from .serlializers import EmployeeSerializer, ProjectSerializer


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
        employee = self.get_object(pk)
        employee.deleted = True
        employee.save()
        return Response(status=status.HTTP_204_NO_CONTENT)



class EmployeeList(generics.ListCreateAPIView):
    """
    List all employees, or create a new employee.
    """
    queryset = Employee.objects.filter(deleted=False)
    serializer_class = EmployeeSerializer


class EmployeeDetail(APIView):
    """
    Retrieve, update or delete an employee identity.
    """
    def get_object(self, pk):
        try:
            return Employee.objects.get(pk=pk)
        except Employee.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        employee = self.get_object(pk)
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        employee = self.get_object(pk)
        serializer = EmployeeSerializer(employee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        employee = self.get_object(pk)
        employee.deleted = True
        employee.save()
        return Response(status=status.HTTP_204_NO_CONTENT)

