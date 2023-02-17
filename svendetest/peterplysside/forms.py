from django.forms import ModelForm
from api.models import *

class ReportForm(ModelForm):
    class Meta:
        model = Rapport
        fields = ('beskrivelse',)


class personForm(ModelForm):
    class Meta:
        model = Person
        fields = ('brugernavn', 'password','adresse','mail','postnummer')