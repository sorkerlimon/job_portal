from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField

     

class Employee_profile(models.Model):

    Education = (
        ('Completed 10 years school', 'Completed 10 years school'),
        ('Completed 10 years school & High School', 'Completed 10 years school & High School'),
        ('University Degree', 'University Degree'),
        ('University Degree - Masters', 'University Degree - Masters'),
        ('Technical Degree', 'Technical Degree'),
        ('Others', 'Others'),

    )
    Computer = (
        ('Yes', 'Yes'),
        ('No', 'No'),
 

    )
    user = models.OneToOneField(User, blank=True, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True, blank=True)
    nid = models.CharField(max_length=200, null=True, blank=True)
    bank_account = models.CharField(max_length=200, null=True, blank=True)
    dob = models.DateField(max_length=8,blank=True,null=True)
    
    email = models.EmailField(max_length=200, unique=True, null=True, blank=True)
    country = CountryField(null=True,blank=True)
    profile_pic = models.ImageField(null=True, blank=True, upload_to='profile/', default="profile/profile.png")
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    
    has_used_secret_key = models.BooleanField(default=False)

    present_address = models.CharField(max_length=200, null=True)
    parmanenet_address = models.CharField(max_length=200, null=True)
    emergency_phone = models.CharField(max_length=200, null=True, blank=True)

    education_degree = models.CharField(max_length=255, blank=True, null=True, choices=Education, default="Completed 10 years school")
    city = models.CharField(max_length=200, null=True)
    working_hours = models.IntegerField(blank=True,null=True)
    have_computer = models.CharField(max_length=255, blank=True, null=True, choices=Computer, default="Yes")
    comment = models.TextField(blank=True, null=True)

    # license = models.BooleanField(default=False)
    
    agreement_1 = models.ImageField(null=True, blank=True, upload_to='agreement/' )
    agreement_2 = models.ImageField(null=True, blank=True, upload_to='agreement/')


    def __str__(self) -> str:
        return self.name
