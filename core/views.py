from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Patient, SOAPNote, DailyMemo
from .forms import PatientForm, SOAPNoteForm, DailyMemoForm

@login_required
def patient_list(request):
    patients = Patient.objects.all().order_by('name')
    return render(request, 'core/patient_list.html', {'patients': patients})

@login_required
def patient_create(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Patient added successfully.')
            return redirect('patient_list')
    else:
        form = PatientForm()
    return render(request, 'core/patient_form.html', {'form': form, 'title': 'Add Patient'})

@login_required
def soap_note_create(request):
    if request.method == 'POST':
        form = SOAPNoteForm(request.POST, request.FILES)
        if form.is_valid():
            soap_note = form.save(commit=False)
            soap_note.created_by = request.user
            soap_note.save()
            messages.success(request, 'SOAP note added successfully.')
            return redirect('patient_detail', pk=soap_note.patient.pk)
    else:
        form = SOAPNoteForm()
    return render(request, 'core/soap_note_form.html', {'form': form, 'title': 'Add SOAP Note'})

@login_required
def patient_detail(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    soap_notes = patient.soap_notes.all()
    return render(request, 'core/patient_detail.html', {
        'patient': patient,
        'soap_notes': soap_notes
    })

@login_required
def daily_memo_create(request):
    if request.method == 'POST':
        form = DailyMemoForm(request.POST)
        if form.is_valid():
            memo = form.save(commit=False)
            memo.created_by = request.user
            memo.save()
            messages.success(request, 'Daily memo added successfully.')
            return redirect('daily_memo_list')
    else:
        form = DailyMemoForm()
    return render(request, 'core/daily_memo_form.html', {'form': form, 'title': 'Add Daily Memo'})

@login_required
def daily_memo_list(request):
    memos = DailyMemo.objects.all().order_by('-date')
    return render(request, 'core/daily_memo_list.html', {'memos': memos})