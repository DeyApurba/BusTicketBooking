from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Passenger(models.Model):
    p_id=models.IntegerField(primary_key=True)
    mob_number=models.CharField(max_length=14)
    addres=models.TextField()
    gender=models.CharField(max_length=6)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
