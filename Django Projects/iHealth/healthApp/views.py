from django.shortcuts import render
from rest_framework import viewsets, generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Patient,Devices,Data_bp5s,Data_hs2s
from .serializers import *

# Create your views here.

class PatientViewSet(viewsets.ModelViewSet):
    """ GET : fetch model records
        POST : create new record
        PUT : update all record fields 
        PATCH : update some record fields
    """
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    # allowed_methods = ['GET','POST','PUT']
    
class SpecificPatientView(generics.ListAPIView):
    """ This Type of View doesn't support POST method """
    serializer_class = PatientSerializer
    def get_queryset(self):
        patient_name = self.kwargs.get('name')
        return Patient.objects.filter(name=patient_name)
    
class DeviceView(APIView):
    def get(self, request):
        try :
            device_name = request.query_params.get('name')
            queryset = Devices.objects.get(name=device_name)
            serializer = DevicesSerializer(queryset, many=False)
            return Response(serializer.data)
        except Exception :
            return Response({"detail": 'ERROR'})
        
    def post(self, request):
        try :
            device, is_created = Devices.objects.get_or_create(name = request.data['name'])
            if (is_created) :
                serializer = DevicesSerializer(data=request.data)
            else : 
                serializer = DevicesSerializer(device, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)
        except :
            # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            return Response({"detail": 'ERROR'})
    
class DataBP5SView(generics.ListCreateAPIView):
    serializer_class = Data_BP5S_Serializer
    def get_queryset(self):
        patient_id = self.request.query_params.get('patient')
        queryset = Data_bp5s.objects.filter(patient__id=patient_id)
        return queryset
    
    def perform_create(self, serializer):
        patient_id = self.request.data.get('patient')
        # For getting the patient, we can use ('pk', 'id' or the specific name of primary key)
        patient = Patient.objects.get(pk=patient_id)
        serializer.save(patient=patient)
        return Response(serializer.data)
    
class DataHS2SView(generics.ListCreateAPIView):
    serializer_class = Data_HS2S_Serializer
    def get_queryset(self):
        patient_id = self.request.query_params.get('patient')
        queryset = Data_hs2s.objects.filter(patient__id=patient_id)
        return queryset
    
    def perform_create(self, serializer):
        patient_id = self.request.data.get('patient')
        # For getting the patient, we can use ('pk', 'id' or the specific name of primary key)
        patient = Patient.objects.get(pk=patient_id)
        serializer.save(patient=patient)
        return Response(serializer.data)