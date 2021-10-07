

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework import generics

from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend

from django.http import Http404

from .models import *
from .serializers import *


class HardwareList(generics.ListCreateAPIView):
    """
    List all hardwares, or create a new hardware tools.
    """
    queryset = Hardware.objects.all()
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filter_fields = ('status', 'type')
    serializer_class = HardwareSerializer


class HardwareDetail(APIView):
    """
    Retrieve, update or delete a hardware tools.
    """
    def get_object(self, pk):
        try:
            return Hardware.objects.get(pk=pk)
        except Hardware.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        hardware = self.get_object(pk)
        serializer = HardwareSerializer(hardware)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        hardware = self.get_object(pk)
        serializer = HardwareSerializer(hardware, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        hardware = self.get_object(pk)
        hardware.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class SoftwareList(generics.ListCreateAPIView):
    """
    List all softwares, or create a new software tools.
    """
    queryset = Software.objects.filter()
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filter_fields = ('type', 'status')
    serializer_class = SoftwareSerializer


class SoftwareDetail(APIView):
    """
    Retrieve, update or delete a software tools.
    """
    #permission_classes = (IsAuthenticated,)
    def get_object(self, pk):
        try:
            return Software.objects.get(pk=pk)
        except Software.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        software = self.get_object(pk)
        serializer = SoftwareSerializer(software)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        software = self.get_object(pk)
        serializer = SoftwareSerializer(software, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        software = self.get_object(pk)
        software.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class DocumentList(generics.ListCreateAPIView):
    """
    List all documents, or create a new document.
    """
    queryset = Document.objects.filter()
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filter_fields = ('status', 'type', 'author')
    serializer_class = DocumentSerializer


class DocumentDetail(APIView):
    """
    Retrieve, update or delete a document.
    """
    #permission_classes = (IsAuthenticated,)
    def get_object(self, pk):
        try:
            return Document.objects.get(pk=pk)
        except Document.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        document = self.get_object(pk)
        serializer = DocumentSerializer(document)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        document = self.get_object(pk)
        serializer = DocumentSerializer(document, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        document = self.get_object(pk)
        document.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class GenericFunctionsList(generics.ListCreateAPIView):
    """
    List all documents, or create a new document.
    """
    queryset = GenericFunction.objects.filter()
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filter_fields = ('status', 'author', 'language')
    serializer_class = GenericFunctionSerializer


class GenericFunctionDetail(APIView):
    """
    Retrieve, update or delete a GenericFunction.
    """
    #permission_classes = (IsAuthenticated,)
    def get_object(self, pk):
        try:
            return GenericFunction.objects.get(pk=pk)
        except GenericFunction.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        gen_function = self.get_object(pk)
        serializer = GenericFunctionSerializer(gen_function)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        gen_function = self.get_object(pk)
        serializer = GenericFunctionSerializer(gen_function, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        gen_function = self.get_object(pk)
        gen_function.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)