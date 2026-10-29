from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import MenuItem,Booking
User=get_user_model()
class MenuItemSerializer(serializers.ModelSerializer):
 class Meta: model=MenuItem; fields=["id","title","price","inventory"]
class BookingSerializer(serializers.ModelSerializer):
 class Meta: model=Booking; fields=["id","first_name","reservation_date","reservation_slot"]
 def validate(self,attrs):
  d=attrs.get("reservation_date",getattr(self.instance,"reservation_date",None)); s=attrs.get("reservation_slot",getattr(self.instance,"reservation_slot",None))
  q=Booking.objects.filter(reservation_date=d,reservation_slot=s)
  if self.instance: q=q.exclude(pk=self.instance.pk)
  if d and s and q.exists(): raise serializers.ValidationError("This date and time slot is already booked.")
  return attrs
class RegistrationSerializer(serializers.ModelSerializer):
 password=serializers.CharField(write_only=True,min_length=8,trim_whitespace=False)
 class Meta: model=User; fields=["id","username","email","password"]
 def create(self,data): return User.objects.create_user(**data)
