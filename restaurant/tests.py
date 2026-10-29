from datetime import date,timedelta
from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token
from rest_framework import status
from .models import Booking,MenuItem
User=get_user_model()
class APIProjectTests(APITestCase):
 def setUp(self):
  self.user=User.objects.create_user(username="customer",password="Pass12345!")
  self.token=Token.objects.create(user=self.user)
  self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.token.key}")
 def test_menu_public(self):
  self.client.credentials(); MenuItem.objects.create(title="Pasta",price="12.50",inventory=5)
  self.assertEqual(self.client.get("/api/menu-items/").status_code,status.HTTP_200_OK)
 def test_customer_cannot_create_menu(self):
  r=self.client.post("/api/menu-items/",{"title":"Pasta","price":"12.50","inventory":5},format="json")
  self.assertEqual(r.status_code,status.HTTP_403_FORBIDDEN)
 def test_booking_create(self):
  r=self.client.post("/api/bookings/",{"first_name":"Asha","reservation_date":(date.today()+timedelta(days=1)).isoformat(),"reservation_slot":"19:00"},format="json")
  self.assertEqual(r.status_code,status.HTTP_201_CREATED)
 def test_duplicate_slot(self):
  d=date.today()+timedelta(days=2); Booking.objects.create(user=self.user,first_name="Asha",reservation_date=d,reservation_slot="19:00")
  r=self.client.post("/api/bookings/",{"first_name":"Mira","reservation_date":d.isoformat(),"reservation_slot":"19:00"},format="json")
  self.assertEqual(r.status_code,status.HTTP_400_BAD_REQUEST)
