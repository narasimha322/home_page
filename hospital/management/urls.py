from django.urls import path, include
from rest_framework.routers import DefaultRouter
from django.conf.urls.static import static
from django.conf import settings

from .views import *

router = DefaultRouter()
router.register(r'doctors', DoctorViewSet)
router.register(r'patients', PatientViewSet)
router.register(r'appointments', AppointmentViewSet)
router.register(r'history', MedicalHistoryViewSet)
router.register(r'tablets', TabletViewSet)
router.register(r'scans', ScanViewSet)
router.register(r'rooms', RoomViewSet)
router.register(r'bills', BillViewSet)
router.register(r'beds', BedViewSet)

urlpatterns = [
    path('', include(router.urls)),
] +static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
