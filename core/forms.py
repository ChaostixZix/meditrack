from django import forms
from .models import Patient, SOAPNote, DailyMemo

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['name', 'bangsal', 'room']

class SOAPNoteForm(forms.ModelForm):
    class Meta:
        model = SOAPNote
        fields = ['patient', 'date', 'subjective', 'objective', 'assessment', 'plan', 'image']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'subjective': forms.Textarea(attrs={'rows': 4}),
            'objective': forms.Textarea(attrs={'rows': 4}),
            'assessment': forms.Textarea(attrs={'rows': 4}),
            'plan': forms.Textarea(attrs={'rows': 4}),
        }

class DailyMemoForm(forms.ModelForm):
    class Meta:
        model = DailyMemo
        fields = ['date', 'content']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }