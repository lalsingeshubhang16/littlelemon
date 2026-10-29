from django.contrib.auth import get_user_model
from django.shortcuts import render
from django.utils.dateparse import parse_date
from rest_framework import generics,permissions,status
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from .models import MenuItem,Booking
from .serializers import MenuItemSerializer,BookingSerializer,RegistrationSerializer
from rest_framework.permissions import BasePermission,SAFE_METHODS
User=get_user_model()
def home(request): return render(request,"restaurant/home.html")
class StaffOrReadOnly(BasePermission):
 def has_permission(self,request,view): return request.method in SAFE_METHODS or bool(request.user and request.user.is_authenticated and request.user.is_staff)
class OwnerOrStaff(BasePermission):
 def has_object_permission(self,request,view,obj): return bool(request.user.is_authenticated and (request.user.is_staff or obj.user_id==request.user.id))
class MenuList(generics.ListCreateAPIView):
 queryset=MenuItem.objects.all().order_by("id"); serializer_class=MenuItemSerializer; permission_classes=[StaffOrReadOnly]
class MenuDetail(generics.RetrieveUpdateDestroyAPIView):
 queryset=MenuItem.objects.all(); serializer_class=MenuItemSerializer; permission_classes=[StaffOrReadOnly]
class BookingList(generics.ListCreateAPIView):
 serializer_class=BookingSerializer; permission_classes=[permissions.IsAuthenticated]
 def get_queryset(self):
  q=Booking.objects.all() if self.request.user.is_staff else Booking.objects.filter(user=self.request.user)
  v=self.request.query_params.get("date")
  if v:
   d=parse_date(v)
   if not d:return Booking.objects.none()
   q=q.filter(reservation_date=d)
  return q
 def perform_create(self,serializer): serializer.save(user=self.request.user)
class BookingDetail(generics.RetrieveUpdateDestroyAPIView):
 serializer_class=BookingSerializer; permission_classes=[permissions.IsAuthenticated,OwnerOrStaff]
 def get_queryset(self): return Booking.objects.all() if self.request.user.is_staff else Booking.objects.filter(user=self.request.user)
@api_view(["POST"])
@permission_classes([permissions.AllowAny])
def register_user(request):
 s=RegistrationSerializer(data=request.data); s.is_valid(raise_exception=True); u=s.save(); t,_=Token.objects.get_or_create(user=u)
 return Response({"id":u.id,"username":u.username,"email":u.email,"token":t.key},status=status.HTTP_201_CREATED)
@api_view(["POST"])
@permission_classes([permissions.IsAuthenticated])
def logout_user(request):
 Token.objects.filter(user=request.user).delete()
 return Response({"message":"Logged out successfully."})
