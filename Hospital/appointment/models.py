from django.db import models

#Create your models here.
class PatientModel(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    name = models.CharField(max_length = 100)
    age = models.IntegerField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    phone_no = models.IntegerField()
    time = models.DateTimeField()
    address = models.CharField(max_length = 100)
    status = models.CharField(max_length = 50, default='Mark Complete', null=True, blank=True)
    email = models.EmailField(default='True')

    
    def __str__(self):
        return self.name
    

