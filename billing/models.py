# billing/models.py

from django.db import models
from uuid import uuid4

class Bill(models.Model):
    bill_id = models.UUIDField(default=uuid4, editable=False, unique=True)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    government_id = models.CharField(max_length=20)
    debt_amount = models.DecimalField(max_digits=12, decimal_places=2)
    debt_due_date = models.DateField()
    debt_id = models.UUIDField()
    sended = models.BooleanField(default=False)

    class Meta:
        unique_together = ('government_id', 'email', 'debt_id')
        constraints = [
            models.UniqueConstraint(fields=['government_id', 'email', 'debt_id'], name="%(app_label)s_%(class)s_unique")
        ]
        indexes = [
            models.Index(fields=['government_id', 'email', 'debt_id'])
        ]

    def __str__(self):
        return f"{self.name} - {self.debt_id}"
