from django.shortcuts import render
from django.core.mail import send_mail
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

            return render(request, 'success.html')

    else:
        form = BookingForm()

    return render(request, 'booking.html', {'form': form})
