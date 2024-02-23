from django.urls import path
from . import views

urlpatterns = [
    path('patient/',views.Patient, name='patient'),
    path('patientform/', views.PatientFormView, name='patientform'),
    path('checkout/', views.checkout, name='checkout'),
    
]  