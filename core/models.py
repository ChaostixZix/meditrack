from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator
from ckeditor.fields import RichTextField

class Patient(models.Model):
    name = models.CharField(max_length=100)
    bangsal = models.CharField(max_length=50)
    room = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

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