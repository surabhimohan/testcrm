from django.urls import path
from .views import *

urlpatterns = [
    path("", login, name='login'),
    path("dashboard", dashboard, name='dashboard')
]