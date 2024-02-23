from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

# Create your views here.



def SignUp(request):
    if request.method == 'POST':  
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')

        data = User.objects.create_user(first_name=first_name, last_name=last_name, username=email, email=email, password=password)
        return redirect('login')
        
            
    return render(request, 'registration.html')

def user_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=email,email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('patient')

    return render(request, 'login.html')


def base(request):
    return render(request,'base.html')