from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .forms import ReportForm, personForm
from random import randint
from django.http import JsonResponse
import requests


# Create your views here.
url1 = 'http://10.130.54.25:8000/data/rjliste/'
url2 = 'http://10.130.54.25:8000/data/personlsite/'
headers = {'X-Requested-With': 'XMLHttpRequest', 'Content-Type': 'application/json',
           'Authorization': 'Token 10221976ae7eebb749b62cb74de527cd6500697a'}



def test(request):
    res = requests.get(url1, headers=headers).json()
    form = ReportForm
    return render(request, "peterplysside/home.html", {"form": ReportForm, "res": res})


def test2(request):
    res = requests.get(url1, headers=headers).json()
    response = requests.get(url2, headers=headers).json()
    form = ReportForm
    return render(request, "peterplysside/home2.html", {"form": ReportForm, "response": response, "res": res})


def test3(request):
    res = requests.get(url1, headers=headers).json()
    response = requests.get(url2, headers=headers).json()
    form = ReportForm
    return render(request, "peterplysside/home3.html", {"form": ReportForm, "response": response, "res": res})


def index(request):
    form = personForm
    if request.method == "POST":
        if request.POST.get('password1') == request.POST.get('password2'):
            saveuser = User.objects.create_user(request.POST.get('username'), password=request.POST.get('password1'))
            saveuser.save()
            return render(request, "peterplysside/index.html", {"form": form, "info": "succes"})

        else:
            return render(request, "peterplysside/index.html", {"form": form, "error": "the password are not matching"})
    else:
        return render(request, "peterplysside/index.html", {"form": form})

