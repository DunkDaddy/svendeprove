from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ReportForm, signupForm, loginForm, passwordRecoveryForm
from django.http import JsonResponse
import requests
from api.models import *


# Create your views here.
url1 = 'http://10.130.54.25:8000/data/rjliste/'
url2 = 'http://10.130.54.25:8000/data/personlsite/'
recover = 'http://10.130.54.25:8000/data/personupdate/1/'
headers = {'X-Requested-With': 'XMLHttpRequest', 'Content-Type': 'application/json',
           'Authorization': 'Token 10221976ae7eebb749b62cb74de527cd6500697a'}
#res = requests.get(url1, headers=headers).json()
#res2 = requests.get(url2, headers=headers).json()
#form = ReportForm


#def test(response):
#    res = requests.get(url1, headers=headers).json()
#    form = ReportForm
#    return render(response, "peterplysside/home.html", {"form": form, "res": res})


#def test2(response):
#    res = requests.get(url1, headers=headers).json()
#    res2 = requests.get(url2, headers=headers).json()
#    form = ReportForm
#    return render(response, "peterplysside/home2.html", {"form": form, "response": res2, "res": res})


#def test3(response):
#    res = requests.get(url1, headers=headers).json()
#    res2 = requests.get(url2, headers=headers).json()
#    form = ReportForm
#    return render(response, "peterplysside/home3.html", {"form": form, "response": res2, "res": res})


def index(response):
    if response.method == "POST":
        check = True
        signup = signupForm(response.POST)
        login = loginForm(response.POST)
        recover = passwordRecoveryForm(response.POST)
        personlist = Person.objects.all()
        if signup.is_valid():
            for person in personlist:
                if signup.cleaned_data['brugernavn'] == person.brugernavn and signup.cleaned_data['password']:
                    signup = signupForm
                    login = loginForm
                    return render(response, "peterplysside/index.html", {"signup": signup, "login": login})
                else:
                    s = Person(navn=signup.cleaned_data["navn"], adresse=signup.cleaned_data["adresse"], mail=signup.cleaned_data["mail"], tlf=signup.cleaned_data["tlf"], postnummer=signup.cleaned_data["postnummer"], cpr=signup.cleaned_data["cpr"], brugernavn=signup.cleaned_data["brugernavn"], password=signup.cleaned_data["password"])
                    for person in personlist:
                        if s.brugernavn == person.brugernavn and s.password == person.password:
                            check = False
                    if check == True:
                        s.save()
                    res = requests.get(url1, headers=headers).json()
                    form = ReportForm
                    x = 233 - (s.point / 3 - 1)
                    return render(response, "peterplysside/home.html", {"form": form, "res": res, "person": s, "purple": x})

        if login.is_valid():
            for person in personlist:
                if login.cleaned_data['brugernavn'] == person.brugernavn and login.cleaned_data['password']:
                    s = person
                    res = requests.get(url1, headers=headers).json()
                    form = ReportForm
                    x = 233 - (s.point / 3 - 1)
                    if s.point > 500:
                        res2 = requests.get(url2, headers=headers).json()
                        return render(response, "peterplysside/home2.html",{"form": form, "res": res, "person": s, "people": res2, "purple": x})
                    else:
                        return render(response, "peterplysside/home.html", {"form": form, "res": res, "person": s, "purple": x})

        if recover.is_valid():
            for person in personlist:
                if recover.cleaned_data['mail'] == person.mail and recover.cleaned_data['tlf'] == person.tlf and recover.cleaned_data['cpr'] == person.cpr:
                    s = person
                    s.password = recover.cleaned_data['password']
                    s.save()
                    signup = signupForm
                    login = loginForm
                    recover = passwordRecoveryForm
                    return render(response, "peterplysside/index.html", {"signup": signup, "login": login, 'recover': recover})


    else:
        signup = signupForm
        login = loginForm
        recover = passwordRecoveryForm
    return render(response, "peterplysside/index.html", {"signup": signup, "login": login, 'recover': recover})


