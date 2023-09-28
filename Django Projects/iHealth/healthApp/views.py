from django.shortcuts import render
from rest_framework import viewsets
from .models import Patient
from .serializers import PatientSerializer

# Create your views here.

class PatientViewSet(viewsets.ModelViewSet):
    """The POST request (field=value) to this view will automaticaly add data to data base
    And GET request will retreive database content"""
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
