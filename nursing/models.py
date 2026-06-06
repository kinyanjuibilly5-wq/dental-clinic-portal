from django.db import models

class Placeholder(models.Model):
    name = models.CharField(max_length=100, blank=True)

    class Meta:
        app_label = 'nursing'


# Placeholders for admin imports
admin_model = []
admin_models = []
