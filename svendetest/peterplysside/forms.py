from django.forms import ModelForm
from api.models import *

class ReportForm(ModelForm):
    class Meta:
        model = Rapport
        fields = ('beskrivelse',)