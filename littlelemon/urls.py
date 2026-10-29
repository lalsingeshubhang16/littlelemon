from django.contrib import admin
from django.urls import path,include
from rest_framework.authtoken.views import obtain_auth_token
from restaurant.views import home,register_user,logout_user
urlpatterns=[path("admin/",admin.site.urls),path("",home),path("api/",include("restaurant.urls")),path("api/registration/",register_user),path("api/token/login/",obtain_auth_token),path("api/token/logout/",logout_user)]
