

from bus.models import Ticket_Booking



from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User


class CreateUserForm(UserCreationForm):
    class Meta:
        model=User
        fields={'username','email','password1','password2'}


class RegistrationForm(UserCreationForm):
    pass


class TicketBookingForm(forms.ModelForm):

    class Meta:
        model=Ticket_Booking
        fields=[

            'from_dist',
            'to_dist',
            'booking_date',
        ]



