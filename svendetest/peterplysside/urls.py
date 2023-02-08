from django.contrib import admin
from django.urls import path
import include
from .views import *

urlpatterns = [
    path('', index)
]