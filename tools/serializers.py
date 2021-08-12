from .models import (Hardware, Software, Document, GenericFunction)
from rest_framework import serializers


class SoftwareSerializer(serializers.ModelSerializer):
    class Meta:
        model = Software
        fields = "__all__"


class HardwareSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hardware
        fields = "__all__"


class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = "__all__"


class GenericFunctionSerializer(serializers.ModelSerializer):
    class Meta:
        model = GenericFunction
        fields = "__all__"