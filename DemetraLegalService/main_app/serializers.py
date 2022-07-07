from rest_framework import serializers
from .models import *


class ServiceListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'


class WorkerListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Worker
        fields = '__all__'


class ClientListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'


class CaseListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Case
        fields = '__all__'


class RequestDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Request
        fields = '__all__'
