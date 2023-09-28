from django.db import models

class Patient(models.Model):
    names = models.CharField(max_length=200, null=False, default="Unknown Patient")
    age = models.IntegerField(null=False, default=0)
    height = models.IntegerField(null=False, default=0)
    sex = models.BooleanField(null=False, default=True)
    
    def __str__(self) -> str:
        return self.names

class Data_hs5s(models.Model):
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
    
    def __str__(self) -> str:
        return self.patient.names
    
class Data_bp5s(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    sys = models.FloatField()
    dia = models.FloatField()
    
    def __str__(self) -> str:
        return self.patient.names
