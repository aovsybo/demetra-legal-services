from django.contrib import admin
from django.urls import path, include
from .views import *


app_name = 'main_app'
urlpatterns = [
    path('services/', ServiceListView.as_view()),
    path('workers/', WorkerListView.as_view()),
    path('clients/', ClientListView.as_view()),
    path('cases/', CaseListView.as_view()),
    path('requests/', RequestDetailView.as_view()),
]
