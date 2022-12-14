


from django.contrib import admin
from django.urls import path
from django.urls import reverse_lazy

import django.contrib.auth.views as auth_views
from django.contrib.auth.views import LoginView,LogoutView
import home.views
from home.views import MyPasswordChangeView,MyPasswordResetDoneView


urlpatterns = [
    path('admin/',admin.site.urls),
    path('', home.views.home_view,name='home'),
    #path('',auth_views.LoginView.as_view(template_name='login.html') ),
    path('home/', home.views.home_view,name='home'),


    path('register/',home.views.registerPage,name="register"),
    path('login/', home.views.loginPage,name="login"),
    path('logout/', home.views.logoutUser,name="logout"),
    path('booking/',home.views.findbus,name='booking'),
    path('list/',home.views.list_view,name='lst'),
    path('bookings/',home.views.bookings,name='bk'),


    path('bus/', home.views.bus_view,name='bus'),
    path('bus/search-bus', home.views.search_bus_view,name='s-bus'),
    path('bus/search-bus/bus-seat-booking', home.views.bus_seat_booking_view,name='bsb'),
    path('bus/search-bus/bus-seat-booking/payment', home.views.payment_view,name='payment'),


    #path('login/home', home.views.home_view,name='home'),
    path('signup/home', home.views.home_view,name='home'),
    path('about/', home.views.about_view,name='about'),


    path('change-password/', MyPasswordChangeView.as_view(), name='password-change-view'),
    path('change-password/done', MyPasswordResetDoneView.as_view(), name='password-change-done-view'),

    path('contact/',home.views.contact_f,name='contact')

]
