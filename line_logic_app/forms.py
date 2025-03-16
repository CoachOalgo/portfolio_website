from django import forms
from .models import DagData

class DagDataForm(forms.ModelForm):
    class Meta:
        model = DagData
        fields = ['title', 'description', 'csv_file']