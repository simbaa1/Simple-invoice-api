from django.db import models
from django.utils import timezone
from django.conf import settings

User = settings.AUTH_USER_MODEL


    

class Invoice(models.Model):
    class Status(models.TextChoices):
        UNPAID = 'Pending'
        PAID = 'Paid'
        CANCELLED = 'Cancelled'
        LATE = 'Late'
        
    invoice_no = models.CharField(max_length=100, unique=True)
    date = models.DateTimeField(default=timezone.now)
    due_date = models.DateTimeField()
    status = models.CharField(default=Status.UNPAID, choices=Status, max_length=20)
    user = models.ForeignKey(User, on_delete=models.PROTECT)

    def save(self, *args, **kwargs):
        if not self.invoice_no:
            self.invoice_no = f"INV#{int(self.date.strftime('%Y%m%d%H%M%S'))}"
        super().save(*args, **kwargs)

    def __str__(self):
        return self.invoice_no
    
    class Meta:
        ordering = ['-date']
    

   

class ItemLine(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete=models.PROTECT, related_name="items")
    description = models.CharField(max_length=200)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    taxed = models.BooleanField()


    def __str__(self):
        return self.decription

    class Meta:
        verbose_name_plural = "ItemLines"
