from django.contrib import admin
from django.urls import path
import include
from .views import *

urlpatterns = [
    #se alle data
    path('postnummerliste/', postNummer_liste),
    path('personlsite/', person_liste),
    path('handlingsliste/', handlinger_liste),
    path('hjliste/', hj_liste),
    path('rapportliste/', rapport_liste),
    path('rjliste/', rj_liste),
    path('pgliste/', pointGrade_liste),
    path('permissionsliste/', permissions_liste),
    path('upliste/', up_liste),
    path('liste/', liste),
    path('cpr/', cprliste),
    path('personapp/<str:pk>/', appperson_view),
    path('settings/', setting),

    #opret data
    path('postnummercreate/', postNummer_create),
    path('personcreate/', person_create),
    path('handlingercreate/', handlinger_create),
    path('hjcreate/', hj_create),
    path('rapportcreate/', rapport_create),
    path('rjcreate/', rj_create),
    path('pgcreate/', pointGrade_create),
    path('permissionscreate/', permissions_create),
    path('upcreate/',up_create),

    #se specifik data
    path('postnr/<int:pk>/', postNummer_view),
    path('person/<int:pk>/', person_view),
    path('personappalt/<str:pk>/', person_view_navn),
    path('handling/<int:pk>/', handlinger_view),
    path('hj/<int:pk>/', hj_view),
    path('rapport/<int:pk>/', rapport_view),
    path('rj/<int:pk>/', rj_view),
    path('pg/<int:pk>/', pointGrade_view),
    path('permissions/<int:pk>', permissions_view),
    path('up/<int:pk>/', up_view),

    #updater specifik data
    path('postnummerupdate/<int:pk>/', postNummer_update),
    path('personupdate/<int:pk>/', person_update),
    path('handlingerupdate/<int:pk>/', handlinger_update),
    path('hjupdate/<int:pk>/', hj_update),
    path('rapportupdate/<int:pk>/', rapport_update),
    path('rjupdate/<int:pk>/', rj_update),
    path('pgupdate/<int:pk>/', pointGrade_update),
    path('permissionsupdate/<int:pk>/', permissions_update),
    path('upupdate/<int:pk>/', up_update),

    #slet specifik data
    path('postnummerdelete/<int:pk>/', postnummer_delete),
    path('persondelete/<int:pk>/', person_delete),
    path('handlingerdelete/<int:pk>/', handlinger_delete),
    path('hjdelete/<int:pk>/', hj_delete),
    path('rapportdelete/<int:pk>', rapport_delete),
    path('rjdelete/<int:pk>/', rj_delete),
    path('pgdelete/<int:pk>', pointGrade_delete),
    path('permissionsdelete/<int:pk>', permissions_delete),
    path('updelete/<int:pk>/', up_delete),

]