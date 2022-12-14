

from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render,redirect
from .forms import CreateUserForm

from django.contrib import messages
from home.forms import RegistrationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth import authenticate, login, logout,update_session_auth_hash
from .forms import TicketBookingForm

from .models import *
from home.models import Bus
from bus.models import BusB
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordChangeView,PasswordResetDoneView
from home.models import Contact

class MyPasswordChangeView(PasswordChangeView):
    template_name ="password-change.html"
    success_url = reverse_lazy('password-change-done-view')

class MyPasswordResetDoneView(PasswordResetDoneView):
    template_name ="password-reset-done.html"

def registerPage(request):
    # if request.user.is_authenticated:
    #     return redirect('home')
    # else:
        form= CreateUserForm()

        if request.method=='POST':
            form=CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user=form.cleaned_data.get('username')
                messages.success(request,'Account is successfully created for ' + user )
                return redirect('login')
        context= {'form': form}
        return render(request,'register.html',context)

def loginPage(request):
    if request.method =='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user=authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.info(request,'username or password is incorrect')

    context= {}
    return render(request,'login.html',context)

def logoutUser(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def home_view(request):
    return render(request, 'home.html')







def bus_view(request):
    return render( request, 'bus.html')
def search_bus_view(request):
    return render( request, 'search_bus.html')
def bus_seat_booking_view(request):
    return   render( request, 'bus_seat_booking.html')



def payment_view(request):
    return  render(request,'payment.html')

def about_view(request):
    return  render(request,'about.html')




@login_required(login_url='login')
def booking(request):
    if(request.method =='POST'):
        form = TicketBookingForm(request.POST)
        form.save()

        return redirect('home')
    form= TicketBookingForm()

    context={
        'booking_form' : form,

    }

    return render(request,'booking.html',context)

# def scheduleDate(request):
#     if (request.method == 'POST'):
#         form = ScheduleForm(request.POST)
#         form.save()
#
#         return redirect('home')
#     form = ScheduleForm()
#
#     context = {
#         'schedule_form': form,
#
#     }
#
#     return render(request, 'schedule_booking.html', context)


def contact_f(request):
    if request.method=="POST":
        contact=Contact()
        name=request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        contact.name=name
        contact.email = email
        contact.subject = subject
        contact.save()
        return HttpResponse("<h1>Thanks for contact</h1>")
    return render(request,'contact.html')


def ticket_booking(request):
    context = {}
    if request.method == 'POST':
        source_r = request.POST.get('source')
        dest_r = request.POST.get('destination')
        date_r = request.POST.get('date')
        bus_list = Bus.objects.filter(source=source_r, dest=dest_r, date=date_r)
        if bus_list:
            return render(request, 'list.html')
        else:
            context["error"] = "Sorry no buses availiable"
            return render(request, 'booking.html', context)
    else:
        return render(request, 'booking.html')




@login_required(login_url='login')
def findbus(request):
    context = {}
    if request.method == 'POST':
        source_r = request.POST.get('source')
        dest_r = request.POST.get('destination')
        date_r = request.POST.get('date')
        bus_list = Bus.objects.filter(source=source_r, dest=dest_r, date=date_r)
        if bus_list:
            return render(request, 'list.html', locals())
        else:
            context["error"] = "Sorry no buses availiable"
            return render(request, 'findbus.html', context)
    else:
        return render(request, 'findbus.html')

def list_view(request):
    return render(request, 'list.html')

def bookings(request):
    return render(request, 'bookings.html')