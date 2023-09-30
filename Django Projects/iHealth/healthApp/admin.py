from django.contrib import admin

from .models import Patient, Data_bp5s, Data_hs2s, Devices


admin.site.register(Patient)
admin.site.register(Data_bp5s)
admin.site.register(Data_hs2s)
admin.site.register(Devices)
