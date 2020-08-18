from django import forms
from covidapplication.models import Covid

class CovidForm(forms.ModelForm):
    class Meta:
        model = Covid
        fields = "__all__"