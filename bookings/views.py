from django.shortcuts import render, redirect
from django.utils.http import urlencode
from .forms import BookingForm


def home(request):
    return render(request, 'home.html')


def services(request):
    return render(request, 'services.html')


def booking_view(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)

        if form.is_valid():
            booking = form.save()

            # ✅ ONLY WHATSAPP (SAFE ON RENDER)
            whatsapp_number = "919255202302"  # without +

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
