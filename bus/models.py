from django.db import models

from passenger.models import Passenger


# Create your models here.

class Bus(models.Model):
    bus_id=models.IntegerField(primary_key=True)
    bus_name=models.CharField(max_length=20)
    bus_type=models.CharField(max_length=5)
    capacity=models.IntegerField()
    passenger = models.ForeignKey(Passenger, on_delete=models.DO_NOTHING)
    #passenger=models.ForeignKey(Passenger,on_delete=models.SET_NULL,null=True)

class BusB(models.Model):
    bus_name = models.CharField(max_length=30)
    source = models.CharField(max_length=30)
    dest = models.CharField(max_length=30)
    nos = models.DecimalField(decimal_places=0, max_digits=2)
    rem = models.DecimalField(decimal_places=0, max_digits=2)
    price = models.DecimalField(decimal_places=2, max_digits=6)
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return self.bus_name

class Schedule(models.Model):
    s_id=models.IntegerField(primary_key=True)
    dprt_loc=models.CharField(max_length=20)
    dest=models.CharField(max_length=20)
    #arrv_time=models.CharField(max_length=5)
    sc_date=models.DateField(null=True)
    dprt_time=models.TimeField(null=True)
    bus=models.ForeignKey(Bus,on_delete=models.CASCADE)

class Ticket_Booking(models.Model):
    booking_id=models.IntegerField(primary_key=True)

    from_dist=models.CharField(max_length=20,default='Null')
    to_dist =models.CharField(max_length=20,default='Null')

    tot_num_seats=models.IntegerField()
    ticket_price=models.IntegerField()
    tot_amount=models.IntegerField()
    booking_date=models.DateField(null=True)
    schedule=models.ForeignKey(Schedule,on_delete=models.CASCADE)
    passenger=models.ForeignKey(Passenger,on_delete=models.SET_NULL,null=True)



class Seats(models.Model):
    seat_id=models.IntegerField(primary_key=True)
    #seat_no = models.IntegerField()


    schedule=models.ForeignKey(Schedule,on_delete=models.SET_NULL,null=True)
    passenger=models.ForeignKey(Passenger,on_delete=models.SET_NULL,null=True)
    ticketbooking=models.ForeignKey(Ticket_Booking,on_delete=models.SET_NULL,null=True)


