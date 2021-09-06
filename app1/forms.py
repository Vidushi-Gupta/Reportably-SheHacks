from django.forms import ModelForm
from .models  import Report
from django import forms 
class ReportForm(ModelForm):
    
    class Meta:
        model= Report
        fields= ['problem', 'location', 'date', 'document', 'complaint_title']
        widgets = {'date': forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),}
