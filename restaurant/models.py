from django.conf import settings
from django.db import models
class MenuItem(models.Model):
 title=models.CharField(max_length=120)
 price=models.DecimalField(max_digits=6,decimal_places=2)
 inventory=models.PositiveIntegerField(default=0)
 def __str__(self): return self.title
class Booking(models.Model):
 TIME_SLOTS=[("17:00","5:00 PM"),("17:30","5:30 PM"),("18:00","6:00 PM"),("18:30","6:30 PM"),("19:00","7:00 PM"),("19:30","7:30 PM"),("20:00","8:00 PM"),("20:30","8:30 PM"),("21:00","9:00 PM")]
 user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name="restaurant_bookings")
 first_name=models.CharField(max_length=80)
 reservation_date=models.DateField(db_index=True)
 reservation_slot=models.CharField(max_length=5,choices=TIME_SLOTS)
 class Meta:
  ordering=["reservation_date","reservation_slot"]
  constraints=[models.UniqueConstraint(fields=["reservation_date","reservation_slot"],name="unique_booking_date_slot")]
