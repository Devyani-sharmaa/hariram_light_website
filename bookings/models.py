from django.db import models

class Booking(models.Model):
    EVENT_CHOICES = [
        ('Wedding', 'Wedding'),
        ('Jagran', 'Jagran'),
        ('Birthday', 'Birthday'),
        ('Other', 'Other'),
    ]

    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    event_type = models.CharField(max_length=20, choices=EVENT_CHOICES)
    event_date = models.DateField()
    address = models.TextField()
    message = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
