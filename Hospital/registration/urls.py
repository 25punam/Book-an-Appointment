from django.urls import path
from . import views

urlpatterns = [

    path('signup/',views.SignUp, name='signup'),
    path('base/',views.base, name='base'),
    
]
