from django.db import models
from django.utils.translation import gettext_lazy as _
from customers.models import Customer
from tables.models import Table


class Reservation(models.Model):
    class Status(models.TextChoices):
        PENDING = "pending", _("В ожидании")
        CONFIRMED = "confirmed", _("Подтвержденно")
        CANCELED = "canceled", _("Отмененно")
        
    
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    date = models.DateField()
    status = models.CharField(max_length=10, choices=Status.choices, default=Status.PENDING)
    
    def __str__(self):
        return f"Бронь для {self.customer.name} на {self.date}"
    