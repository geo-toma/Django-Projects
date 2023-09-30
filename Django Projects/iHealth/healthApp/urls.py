from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PatientViewSet, DeviceView, DataBP5SView, DataHS2SView, SpecificPatientView

router = DefaultRouter()
router.register(r'patients', PatientViewSet)

urlpatterns = [
    path('', include(router.urls)),
    # path('patients', PatientViewSet.as_view(), name='patient-data'),
    path('patient/<str:name>', SpecificPatientView.as_view(), name='patient-data'),
    path('device', DeviceView.as_view(), name='device-data'),
    path('data/bp5s', DataBP5SView.as_view(), name='bp5s-data'),
    path('data/hs2s', DataHS2SView.as_view(), name='hs2s-data'),
]