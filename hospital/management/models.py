from django.db import models
from django.utils import timezone
GENDER_CHOICES = (('M', 'Male'), ('F', 'Female'), ('O', 'Other'))

from django.db import models
from django.utils import timezone

GENDER_CHOICES = (('M', 'Male'), ('F', 'Female'), ('O', 'Other'))
class Doctor(models.Model):
    name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    profile = models.ImageField(upload_to='doctors/', null=True, blank=True)

    def __str__(self):
        return self.name


class Patient(models.Model):
    name=models.CharField(max_length=20)
    id = models.AutoField(primary_key=True)
    phone = models.CharField(max_length=15, unique=True)
    email = models.EmailField()
    age = models.PositiveIntegerField()
    city = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    appointment_date = models.DateTimeField(default=timezone.now)  # Updated to DateTimeField for date and time selection

    def __str__(self):
        return f"Appointment with {self.patient.name} for {self.doctor.name} on {self.appointment_date.strftime('%Y-%m-%d %H:%M')}"

class MedicalHistory(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    condition = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"medical  {self.patient.name}" 

class Tablet(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    dosage = models.CharField(max_length=100)
    def __str__(self):
        return f"Tablet  {self.patient.name}" 

class Scan(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    scan_type = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self):
        return f"Scan  {self.patient.name}" 

class Room(models.Model):
    room_number = models.CharField(max_length=10, unique=True)
    total_beds = models.IntegerField()

    def __str__(self):
        return f"Room {self.room_number}"

    def available_beds(self):
        return self.beds.filter(is_occupied=False).count()


class Bed(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='beds')
    bed_number = models.CharField(max_length=10)
    is_occupied = models.BooleanField(default=False)
    patient = models.ForeignKey('Patient', on_delete=models.SET_NULL, null=True, blank=True, related_name='beds')
    bed_charge = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    class Meta:
        unique_together = ('room', 'bed_number')  # No duplicate bed in same room

    def __str__(self):
        return f"Bed {self.bed_number} in Room {self.room.room_number}"

from django.db import models
from .models import Doctor, Patient, Bed  # Make sure you import your models

class Bill(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    bed_charges = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    scan_charges = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    report_charges = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    xray_charges = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    initial_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    balance_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return f"Bill for {self.patient.name} with {self.doctor.name}, Total: {self.total_amount}"

    def save(self, *args, **kwargs):
        
        bed = Bed.objects.filter(patient=self.patient).first()
        self.bed_charges = bed.bed_charge if bed else 0

        self.total_amount = (
            self.bed_charges +
            self.scan_charges +
            self.report_charges +
            self.xray_charges
        )

 
        self.balance_amount = self.total_amount - self.initial_amount

        super().save(*args, **kwargs)

    def is_ready_for_discharge(self):
        return self.balance_amount == 0
