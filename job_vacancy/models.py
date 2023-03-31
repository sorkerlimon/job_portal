from django.db import models
from django.contrib.auth.models import User
from users.models import *
        

class Employee_CV(models.Model):

    Country = (
        ('Where are you from?', 'Where are you from?'),
        ('Bangladesh', 'Bangladesh'),
        ('India', 'India'),
        ('Srilanka', 'Srilanka'),
        ('Nepal', 'Nepal'),
        ('Kenya', 'Kenya'),



    )
    Intersted = (
        ('WFH', 'WFH'),
        ('WFO', 'WFO'),
 
    )

    ShiftTime = (
        ('Morning', 'Morning'),
        ('Evening', 'Evening'),
        ('Night', 'Night'),

   
    )
    Education = (
        ('Completed 10 years school', 'Completed 10 years school'),
        ('Completed 10 years school & High School', 'Completed 10 years school & High School'),
        ('University Degree', 'University Degree'),
        ('University Degree - Masters', 'University Degree - Masters'),
        ('Technical Degree', 'Technical Degree'),
        ('Others', 'Others'),

    )
    p_user = models.OneToOneField(Employee_profile, on_delete=models.CASCADE)
    cv = models.FileField(upload_to='cv/')
    uploaded_on = models.DateTimeField(auto_now_add=True)
    meet_link_sent = models.BooleanField(default=False)

    country = models.CharField(max_length=255, blank=True, null=True, choices=Country, default="Where are you from?")
    interestedfor = models.CharField(max_length=255, blank=True, null=True, choices=Intersted, default="WFH")
    fullname = models.CharField(max_length=255, blank=True, null=True)
    phonenumber = models.CharField(max_length=255, blank=True, null=True)
    dateofbirth = models.DateField(blank=True, null=True)
    education = models.CharField(max_length=255, blank=True, null=True, choices=Education, default="Completed 10 years school")
    nationalid = models.CharField(max_length=255, blank=True)

    startingdate = models.DateField(blank=True, null=True)
    shifttime = models.CharField(max_length=255, blank=True, null=True, choices=ShiftTime, default="Day")

    agreementlicens = models.BooleanField(default=False)


    



    def __str__(self) -> str:
        return  f"{self.p_user}"


 

class Documents_upload(models.Model):

    
    p_user = models.OneToOneField(Employee_profile, on_delete=models.CASCADE)
    nid_birthcertificate = models.FileField(upload_to='documents/')
    education_certificate = models.FileField(upload_to='documents/')
    chairman_certificate = models.FileField(upload_to='documents/')
    testimonial = models.FileField(upload_to='documents/')





    def __str__(self) -> str:
        return  f"{self.p_user}"
