from django.forms import ModelForm
from api.models import *

class ReportForm(ModelForm):
    class Meta:
        model = Rapport
        fields = ('beskrivelse',)


class signupForm(ModelForm):
    class Meta:
        model = Person
        fields = ('navn','adresse','mail','tlf','postnummer','cpr','brugernavn','password')


class loginForm(ModelForm):
    class Meta:
        model = Person
        fields = ('brugernavn', 'password')


class passwordRecoveryForm(ModelForm):
    class Meta:
        model = Person
        fields = ('mail', 'tlf', 'cpr', 'password')