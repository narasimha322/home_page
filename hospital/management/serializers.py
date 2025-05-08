from rest_framework import serializers
from .models import *

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'

class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = '__all__'

class MedicalHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalHistory
        fields = '__all__'

class TabletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tablet
        fields = '__all__'

class ScanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Scan
        fields = '__all__'

class RoomSerializer(serializers.ModelSerializer):
    is_bed_available = serializers.SerializerMethodField()

    def get_is_bed_available(self, obj):
        return obj.is_bed_available()

    class Meta:
        model = Room
        fields = '__all__'

class BillSerializer(serializers.ModelSerializer):
    is_ready_for_discharge = serializers.SerializerMethodField()

    def get_is_ready_for_discharge(self, obj):
        return obj.is_ready_for_discharge()

    def create(self, validated_data):
        patient = validated_data['patient']

        # Fetch and sum up charges dynamically
        scan_charges = Scan.objects.filter(patient=patient).aggregate(total=models.Sum('price'))['total'] or 0
        bed_charges = 1000  # Example fixed cost, or fetch from Room model
        report_charges = 500  # Or calculate dynamically if needed
        xray_charges = 750  # Optional logic for x-ray

        initial_amount = bed_charges + scan_charges + report_charges + xray_charges
        balance_amount = initial_amount  # You can later subtract payments

        # Inject calculated values into validated_data
        validated_data.update({
            'bed_charges': bed_charges,
            'scan_charges': scan_charges,
            'report_charges': report_charges,
            'xray_charges': xray_charges,
            'initial_amount': initial_amount,
            'balance_amount': balance_amount,
        })

        return super().create(validated_data)

    class Meta:
        model = Bill
        fields = '__all__'
