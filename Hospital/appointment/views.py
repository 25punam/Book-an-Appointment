from django.core.mail import send_mail
from django.shortcuts import render, redirect
from .models import  PatientModel
from .forms import PatientForm
# Create your views here.
def Patient(request):
    #check request type if post -> status change
    if request.method == 'POST':
        patient_id = request.POST.get('patient_id')
        data = PatientModel.objects.get(id=patient_id)
        data.status = 'Complete'
        data.save()
    

    context = {}
    # patient_obj = PatientModel.objects.all()
    # context['patient'] = patient_obj
    patients = PatientModel.objects.filter(status='Mark Complete').order_by('time') #use filter->pending or exclude->completed on status
    context['patients'] = patients
    return render(request, 'table.html',context)

def PatientFormView(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            patient = form.save()
            email = patient.email
            send_mail(
                'Appointment Confirmation',
                'Thank you for booking your appointment with us!',
                '25punamgode@gmail.com',  
                [email],     # Use the patient's email from the form
                fail_silently=False,
            )
            return redirect('patient')
        else:
            error_message = "Invalid credentials. Please try again."
            return render(request, 'form.html', {'error_message': error_message})

        
    return render(request, 'form.html')

def checkout(request):
    context = {}
    patient_obj = PatientModel.objects.filter(status='Complete')
    context['patient'] = patient_obj
    return render(request,'checkout.html',context)

