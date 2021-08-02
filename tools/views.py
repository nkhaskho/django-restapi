

from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import generics

from django.http import HttpResponse, Http404

from .models import Hardware, Software
from .serlializers import SoftwareSerializer, HardwareSerializer


class HardwareList(generics.ListCreateAPIView):
    """
    List all hardwares, or create a new hardware tools.
    """
    queryset = Hardware.objects.all()
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
    serializer_class = SoftwareSerializer


class SoftwareDetail(APIView):
    """
    Retrieve, update or delete a software tools.
    """
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