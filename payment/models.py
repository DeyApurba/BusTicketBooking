from django.db import models

from bus.models import Ticket_Booking
from passenger.models import Passenger


# Create your models here.

class Payment(models.Model):
    payment_id=models.IntegerField()
    #amount=models.IntegerField()
    #amount_type=models.TextField(max_length=10)
    passenger=models.ForeignKey(Passenger,on_delete=models.SET_NULL,null=True)
    #ticket_booking = models.ForeignKey(Ticket_Booking, on_delete=models.SET_NULL, null=True)