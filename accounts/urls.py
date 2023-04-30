from django.urls import path
from .views import loginuser, logoutuser, register

app_name = 'accounts'

urlpatterns = [
    path("", loginuser, name='loginuser'),
    path('login/', loginuser, name='loginuser'),
    path('logout/', logoutuser, name='logoutuser'),
    path('register/',register, name='register'),
]