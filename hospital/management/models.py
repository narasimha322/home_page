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
        return f"Appointment with {self.name} on {self.appointment_date}"

class MedicalHistory(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    condition = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"medical  {self.name}" 

class Tablet(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    dosage = models.CharField(max_length=100)
    def __str__(self):
        return f"Tablet  {self.name}" 

class Scan(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    scan_type = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self):
        return f"Scan  {self.name}" 

class Room(models.Model):
    room_number = models.CharField(max_length=10, unique=True)
    total_beds = models.IntegerField()
    available_beds = models.IntegerField()
    def __str__(self):
        return f"Room for {self.name}" 

    def is_bed_available(self):
        return self.available_beds > 0

class Bill(models.Model):
    patient = models.OneToOneField(Patient, on_delete=models.CASCADE)
    bed_charges = models.DecimalField(max_digits=10, decimal_places=2)
    scan_charges = models.DecimalField(max_digits=10, decimal_places=2)
    report_charges = models.DecimalField(max_digits=10, decimal_places=2)
    xray_charges = models.DecimalField(max_digits=10, decimal_places=2)
    initial_amount = models.DecimalField(max_digits=10, decimal_places=2)
    balance_amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Bill for {self.name}" 

    def is_ready_for_discharge(self):
        return self.balance_amount == 0
