from django.contrib import admin
from .models import Doctor, Patient, Appointment, MedicalHistory, Tablet, Scan, Room, Bill,Bed


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'specialization', 'age', 'email', 'phone', 'gender']
    search_fields = ['name', 'specialization', 'email', 'phone']
    list_filter = ['gender']


@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ['name','id', 'phone', 'email', 'age', 'city']
    search_fields = ['phone', 'email', 'city']


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ['id', 'patient', 'doctor', 'appointment_date']
    list_filter = ['appointment_date']
    search_fields = ['patient__phone', 'doctor__name']


@admin.register(MedicalHistory)
class MedicalHistoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'patient', 'condition', 'created_at']
    list_filter = ['created_at']
    search_fields = ['patient__phone', 'condition']


@admin.register(Tablet)
class TabletAdmin(admin.ModelAdmin):
    list_display = ['id', 'patient', 'name', 'dosage']
    search_fields = ['name', 'patient__phone']


@admin.register(Scan)
class ScanningAdmin(admin.ModelAdmin):
    list_display = ['id', 'patient', 'scan_type', 'price']
    search_fields = ['scan_type', 'patient__phone']


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ['room_number', 'total_beds', 'available_beds_display']

    def available_beds_display(self, obj):
        return obj.available_beds()
    available_beds_display.short_description = 'Available Beds'

@admin.register(Bed)
class BedAdmin(admin.ModelAdmin):
    list_display = ['bed_number', 'room', 'is_occupied', 'patient']
    list_filter = ['room', 'is_occupied']


@admin.register(Bill)
class BillAdmin(admin.ModelAdmin):
    list_display = ['id', 'patient', 'bed_charges', 'scan_charges', 'report_charges', 'xray_charges', 'initial_amount', 'balance_amount']
    search_fields = ['patient__phone']
