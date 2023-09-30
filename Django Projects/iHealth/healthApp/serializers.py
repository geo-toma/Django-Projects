from rest_framework import serializers
from .models import Patient,Devices,Data_bp5s,Data_hs2s

class PatientSerializer(serializers.ModelSerializer):
    class Meta :
        model = Patient
        fields = '__all__'
    
    # def create(self, validated_data):
    #     name = validated_data.get('name')
    #     if Patient.objects.filter(name=name).exists():
    #         raise serializers.ValidationError("Patient already exists")
    #     return super().create(validated_data)
        
class DevicesSerializer(serializers.ModelSerializer):
    class Meta :
        model = Devices
        fields = '__all__'
        
class Data_HS2S_Serializer(serializers.ModelSerializer):
    class Meta :
        model = Data_hs2s
        fields = '__all__'
        
class Data_BP5S_Serializer(serializers.ModelSerializer):
    class Meta :
        model = Data_bp5s
        fields = '__all__'