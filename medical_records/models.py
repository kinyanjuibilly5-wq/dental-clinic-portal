from django.db import models

class Prescription(models.Model):
    patient = models.ForeignKey('patients.Patient', on_delete=models.CASCADE, null=True)
    doctor = models.ForeignKey('accounts.User', on_delete=models.CASCADE, null=True)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        app_label = 'medical_records'

class MedicalRecord(models.Model):
    patient = models.ForeignKey('patients.Patient', on_delete=models.CASCADE)
    record_date = models.DateTimeField(auto_now_add=True)
    diagnosis = models.TextField(blank=True)

    class Meta:
        app_label = 'medical_records'


# Placeholders for admin imports
admin_model = []
admin_models = []
