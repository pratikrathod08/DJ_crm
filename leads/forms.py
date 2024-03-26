from django import forms  
from .models import Lead


class LeadMOdelForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = (
            
        )


class LeadForm(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    age = forms.IntegerField()