from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.utils.http import urlencode
from .forms import BookingForm
import os


def home(request):
    return render(request, 'home.html')


def services(request):
    return render(request, 'services.html')


def booking_view(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)

        if form.is_valid():
            booking = form.save()

            # 📩 Send Email
            send_mail(
                subject='New Booking Received - Jyoti Lights (Karnal)',
                message=f"""
New Booking Details:

Name: {booking.name}
Phone: {booking.phone}
Email: {booking.email}
Event Type: {booking.event_type}
Event Date: {booking.event_date}
Address: {booking.address}
Message: {booking.message}

Booking Time: {booking.created_at}
                """,
                from_email=os.getenv('EMAIL_HOST_USER'),
                recipient_list=[os.getenv('EMAIL_HOST_USER')],
                fail_silently=False,
            )

            # 📲 WhatsApp Auto Message
            whatsapp_number = "919255202302"  # 👈 Yahan apna number daalo (without +)

            text = f"""
New Booking - HARI RAM Lights

Name: {booking.name}
Phone: {booking.phone}
Email: {booking.email}
Event: {booking.event_type}
Date: {booking.event_date}
Address: {booking.address}
Message: {booking.message}
"""

            encoded_message = urlencode({"text": text})
            whatsapp_url = f"https://wa.me/{whatsapp_number}?{encoded_message}"

            return redirect(whatsapp_url)

    else:
        form = BookingForm()

    return render(request, 'booking.html', {'form': form})
