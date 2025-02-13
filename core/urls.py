from django.urls import path
from . import views

urlpatterns = [
    path('', views.patient_list, name='patient_list'),
    path('patient/add/', views.patient_create, name='patient_create'),
    path('patient/<int:pk>/', views.patient_detail, name='patient_detail'),
    path('soap-note/add/', views.soap_note_create, name='soap_note_create'),
    path('daily-memo/', views.daily_memo_list, name='daily_memo_list'),
    path('daily-memo/add/', views.daily_memo_create, name='daily_memo_create'),
]