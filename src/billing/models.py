from django.db import models
from django.db.models.functions import Now
from django.conf import settings

User = settings.AUTH_USER_MODEL


    

class Invoice(models.Model):
    class Status(models.TextChoices):
        UNPAID = 'Pending'
        PAID = 'Paid'
        CANCELLED = 'Cancelled'
        LATE = 'Late'
        
    invoice_no = models.CharField(max_length=100)
    date = models.DateTimeField(default=Now())
    due_date = models.DateTimeField()
    status = models.CharField(default=Status.UNPAID, choices=Status, max_length=20)
    user = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return self.invoice_no
    

   

class ItemLine(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete=models.PROTECT, related_name="items")
    description = models.CharField(max_length=200)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    taxed = models.BooleanField()


    def __str__(self):
        return self.decription
