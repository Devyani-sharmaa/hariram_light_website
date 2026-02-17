from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # 👈 Ab homepage open hoga
    path('services/', views.services, name='services'),
    path('booking/', views.booking_view, name='booking'),
]
