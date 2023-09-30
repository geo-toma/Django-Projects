from django.db import models

class Patient(models.Model):
    name = models.CharField(max_length=200, null=False, unique=True)
    age = models.IntegerField(null=False, default=0)
    height = models.IntegerField(null=False, default=0)
    gender = models.BooleanField(null=False, default=True)
    
    def __str__(self) -> str:
        return self.name
    
class Devices(models.Model):
    DEVICE_CHOICES = (
        ('HS2S', 'Balance impédancemètre'),
        ('BP5S', 'Tensiomètre'),
        ('BG5S', 'Glucomètre'),
        ('PO3M', 'Oximètre de Pouls'),
    )
    name = models.CharField(primary_key=True, max_length=4, choices=DEVICE_CHOICES)
    mac = models.CharField(max_length=16)
    

class Data_hs2s(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    weight = models.FloatField()
    IMC = models.FloatField()
    body_fat = models.FloatField()
    muscle = models.FloatField()
    bone_salt_content = models.FloatField()
    water = models.FloatField()
    protein = models.FloatField()
    visceral_fat_grade = models.FloatField()
    basal_metabolism = models.FloatField()
    physical_age = models.IntegerField()
    measure_date = models.DateTimeField(auto_now=True, null=False)
    
    def __str__(self) -> str:
        return self.patient.name
    
class Data_bp5s(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    sys = models.FloatField()
    dia = models.FloatField()
    measure_date = models.DateTimeField(auto_now=True, null=False)
    
    def __str__(self) -> str:
        return self.patient.name
