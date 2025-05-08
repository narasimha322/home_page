from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    DoctorViewSet, PatientViewSet, AppointmentViewSet, MedicalHistoryViewSet,
    TabletViewSet, ScanViewSet, RoomViewSet, BillViewSet
)

router = DefaultRouter()
router.register(r'doctors', DoctorViewSet)
router.register(r'patients', PatientViewSet)
router.register(r'appointments', AppointmentViewSet)
router.register(r'history', MedicalHistoryViewSet)
router.register(r'tablets', TabletViewSet)
router.register(r'scans', ScanViewSet)
router.register(r'rooms', RoomViewSet)
router.register(r'bills', BillViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
