from django.shortcuts import render
from rest_framework import generics
from .serializers import ServiceListSerializer, WorkerListSerializer, ClientListSerializer, CaseListSerializer, RequestDetailSerializer
from .models import *
# Create your views here.


class ServiceListView(generics.ListAPIView):
    serializer_class = ServiceListSerializer
    queryset = Service.objects.all()


class WorkerListView(generics.ListAPIView):
    serializer_class = WorkerListSerializer
    queryset = Worker.objects.all()


class ClientListView(generics.ListAPIView):
    serializer_class = ClientListSerializer
    queryset = Client.objects.all()


class CaseListView(generics.ListAPIView):
    serializer_class = CaseListSerializer
    queryset = Case.objects.all()


class RequestDetailView(generics.CreateAPIView):
    serializer_class = RequestDetailSerializer
    # Сделать отправление на почту
