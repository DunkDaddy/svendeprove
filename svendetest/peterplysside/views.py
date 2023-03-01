from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ReportForm, signupForm, loginForm, passwordRecoveryForm
from django.http import JsonResponse
import requests
from api.models import *


# Create your views here.
rjListe = 'http://10.130.54.25:8000/data/rjliste/'
personListe = 'http://10.130.54.25:8000/data/personlsite/'
recover = 'http://10.130.54.25:8000/data/personupdate/1/'
govermentHandling = 'http://10.130.54.25:8000/data/handlingsliste/'
headers = {'X-Requested-With': 'XMLHttpRequest', 'Content-Type': 'application/json',
           'Authorization': 'Token 2183c1ad82ed9ec825dab900e3d78378b3c61f5e'}
highprofile = False

#res = requests.get(url1, headers=headers).json()
#res2 = requests.get(url2, headers=headers).json()
#form = ReportForm


#def test(response):
#    res = requests.get(rjListe, headers=headers).json()
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

currentuser = ""
def index(response):
    if response.method == "POST":
        global currentuser;
        check = True
        signup = signupForm(response.POST)
        login = loginForm(response.POST)
        recover = passwordRecoveryForm(response.POST)
        report = ReportForm(response.POST)
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
                    res = requests.get(rjListe, headers=headers).json()
                    report = ReportForm
                    x = 233 - (s.point / 3 - 1)
                    return render(response, "peterplysside/home.html", {"report": report, "res": res, "person": s, "purple": x})

        if login.is_valid():
            for person in personlist:
                if login.cleaned_data['brugernavn'] == person.brugernavn and login.cleaned_data['password']:
                    s = person
                    res = requests.get(rjListe, headers=headers).json()
                    report = ReportForm
                    x = 233 - (s.point / 3 - 1)
                    currentuser = s
                    res2 = requests.get(personListe, headers=headers).json()
                    govermentsector = WorkSector.objects.get(id=1)
                    if s.worksector == govermentsector:
                        res3 = requests.get(govermentHandling, headers=headers).json()
                        return render(response, "peterplysside/home3.html", {"report": report, "res": res, "person": s, "people": res2, "purple": x,"handling": res3})
                    elif s.point > 500:
                        highprofile = True
                        return render(response, "peterplysside/home2.html", {"report": report, "res": res, "person": s, "people": res2, "purple": x})
                    else:
                        highprofile = False
                        return render(response, "peterplysside/home.html", {"report": report, "res": res, "person": s, "purple": x})

        if recover.is_valid():
            for person in personlist:
                if recover.cleaned_data['mail'] == person.mail and recover.cleaned_data['tlf'] == person.tlf and recover.cleaned_data['cpr'] == person.cpr:
                    s = person
                    s.password = recover.cleaned_data['password']
                    s.save()
                    signup = signupForm
                    login = loginForm
                    recover = passwordRecoveryForm
                    currentuser = person
                    return render(response, "peterplysside/index.html", {"signup": signup, "login": login, 'recover': recover})

        if report.is_valid():
            x = response.POST['suspect']
            suspect = Person.objects.get(id=x)
            reportform = Rapport(beskrivelse=report.cleaned_data['beskrivelse'])
            reportform.save()
            rJunction = Rapport_junctions(rapportId=reportform, snitchId=currentuser, suspectId=suspect)
            rJunction.save()
            s = currentuser
            res = requests.get(rjListe, headers=headers).json()
            report = ReportForm
            x = 233 - (s.point / 3 - 1)
            res2 = requests.get(personListe, headers=headers).json()
            govermentsector = WorkSector.objects.get(id=1)
            if s.worksector == govermentsector:
                res3 = requests.get(govermentHandling, headers=headers).json()
                return render(response, "peterplysside/home3.html",{"report": report, "res": res, "person": s, "people": res2, "purple": x, "handling": res3})
            elif s.point > 500:
                return render(response, "peterplysside/home2.html",{"report": report, "res": res, "person": s, "people": res2, "purple": x})
            else:
                return render(response, "peterplysside/home.html",{"report": report, "res": res, "person": s, "purple": x})

    if response.method == "POST":
        x = response.POST.get('handlingsraport', False)
        rJunction = Rapport_junctions.objects.get(id=x)
        rapport = Rapport.objects.get(id=rJunction.rapportId.id)
        rapport.godtaget = True
        rapport.save()

        s = currentuser
        res2 = requests.get(personListe, headers=headers).json()
        res3 = requests.get(govermentHandling, headers=headers).json()
        res = requests.get(rjListe, headers=headers).json()
        report = ReportForm
        x = 233 - (s.point / 3 - 1)
        return render(response, "peterplysside/home3.html", {"report": report, "res": res, "person": s, "people": res2, "purple": x, "handling": res3})

    else:
        signup = signupForm
        login = loginForm
        recover = passwordRecoveryForm
        currentuser = ""
    return render(response, "peterplysside/index.html", {"signup": signup, "login": login, 'recover': recover})

