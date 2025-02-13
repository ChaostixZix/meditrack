from django import forms
from .models import Patient, SOAPNote, DailyMemo, DPJP
from django_select2.forms import Select2Widget

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['medical_record_number', 'name', 'date_of_birth', 'date_of_admission', 'bangsal', 'room', 'dpjp']
        widgets = {
            'medical_record_number': forms.TextInput(attrs={'placeholder': 'Optional', 'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'date_of_birth': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'date_of_admission': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'bangsal': forms.TextInput(attrs={'class': 'form-control'}),
            'room': forms.TextInput(attrs={'class': 'form-control'}),
            'dpjp': Select2Widget(attrs={'class': 'form-control'})
        }

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