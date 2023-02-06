from django.contrib import admin
from django.urls import path
import include
from .views import *

urlpatterns = [
    #se alle data
    path('postnummerliste/', postNummer_liste),
    path('personlsite/', person_liste),

    #opret data
    path('postnummercreate/', postNummer_create),
    path('personcreate/', person_create),

    #se specifik data
    path('postnr/<int:pk>/', postNummer_view),
    path('person/<int:pk>/', person_view),

    #updater specifik data
    path('postnummerupdate/<int:pk>/', postNummer_update),
    path('personupdate/<int:pk>/', person_update),

    #slet specifik data
    path('postnummerdelete/<int:pk>/', postnummer_delete),
    path('persondelete/<int:pk>/', person_delete)

]