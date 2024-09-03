from django.db import models

class Payment(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=3, default='USD')
    description = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)