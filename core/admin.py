from django.contrib import admin
from .models import DPJP, Patient, SOAPNote, DailyMemo, UserProfile

@admin.register(DPJP)
class DPJPAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_active', 'created_at', 'updated_at')
    list_filter = ('is_active',)
    search_fields = ('name',)
    ordering = ('name',)

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('name', 'medical_record_number', 'age', 'bangsal', 'room', 'dpjp')
    list_filter = ('bangsal', 'dpjp')
    search_fields = ('name', 'medical_record_number')

@admin.register(SOAPNote)
class SOAPNoteAdmin(admin.ModelAdmin):
    list_display = ('patient', 'date', 'created_by')
    list_filter = ('date', 'created_by')
    search_fields = ('patient__name',)

@admin.register(DailyMemo)
class DailyMemoAdmin(admin.ModelAdmin):
    list_display = ('date', 'created_by')
    list_filter = ('date', 'created_by')

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'role')
    list_filter = ('role',)
    search_fields = ('user__username',)