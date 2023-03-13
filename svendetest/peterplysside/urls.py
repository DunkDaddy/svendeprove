from django.contrib import admin
from django.urls import path
import include
from .views import *

urlpatterns = [
    #path('1', test, name='home'),
    #path('2', test2, name='home2'),
    #path('3', test3, name='home3'),
    path('', index, name='index'),
]

