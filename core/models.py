from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator
from ckeditor.fields import RichTextField
from django.utils import timezone

class DPJP(models.Model):
    name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"dr. {self.name}"

    class Meta:
        verbose_name = 'DPJP'
        verbose_name_plural = 'DPJPs'
        ordering = ['name']

class Patient(models.Model):
    medical_record_number = models.CharField(max_length=50, blank=True, null=True)
    name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True)
    age = models.IntegerField(blank=True, null=True)
    date_of_admission = models.DateField(default=timezone.now)
    bangsal = models.CharField(max_length=50)
    room = models.CharField(max_length=20)
    dpjp = models.ForeignKey(DPJP, on_delete=models.PROTECT, verbose_name='DPJP')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if self.date_of_birth:
            today = self.date_of_admission or self.created_at.date()
            self.age = today.year - self.date_of_birth.year - ((today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day))
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} - Room {self.room}"

class SOAPNote(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='soap_notes')
    date = models.DateField()
    subjective = models.TextField()
    objective = models.TextField()
    assessment = models.TextField()
    plan = models.TextField()
    image = models.ImageField(
        upload_to='soap_images/',
        blank=True,
        validators=[FileExtensionValidator(['jpg', 'jpeg', 'png'])],
        max_length=255
    )
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return f"SOAP Note for {self.patient.name} on {self.date}"

class DailyMemo(models.Model):
    date = models.DateField()
    content = RichTextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return f"Memo on {self.date}"

class UserProfile(models.Model):
    ROLE_CHOICES = (
        ('doctor', 'Doctor'),
        ('nurse', 'Nurse'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)

    def __str__(self):
        return f"{self.user.username} - {self.get_role_display()}"