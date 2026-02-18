from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.utils.http import urlencode
from .forms import BookingForm
import logging

logger = logging.getLogger(__name__)


def home(request):
    return render(request, 'home.html')


def services(request):
    return render(request, 'services.html')


def booking_view(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)

        if form.is_valid():
            booking = form.save()

            # ================= EMAIL (SAFE MODE) =================
            try:
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
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=[settings.EMAIL_HOST_USER],
                    fail_silently=True,   # 🔥 VERY IMPORTANT (500 error fix)
                )
            except Exception as e:
                logger.error(f"Email error: {e}")

            # ================= WHATSAPP REDIRECT =================
            whatsapp_number = "919255202302"  # apna number (without +)

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
