from django.db import models

class MedicineDispensing(models.Model):
    prescription = models.ForeignKey('medical_records.Prescription', on_delete=models.CASCADE, null=True)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        app_label = 'pharmacy'


# Placeholder for admin import
admin_models = []


# Placeholders for admin imports
admin_model = []
admin_models = []

class Pharmacist(models.Model):
    user = models.OneToOneField('accounts.User', on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100)

    class Meta:
        app_label = 'pharmacy'
