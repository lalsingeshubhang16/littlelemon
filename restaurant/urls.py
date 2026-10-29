from django.urls import path
from .views import MenuList,MenuDetail,BookingList,BookingDetail
urlpatterns=[path("menu-items/",MenuList.as_view()),path("menu-items/<int:pk>/",MenuDetail.as_view()),path("bookings/",BookingList.as_view()),path("bookings/<int:pk>/",BookingDetail.as_view())]
