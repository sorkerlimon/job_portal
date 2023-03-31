from django.forms import ModelForm,CheckboxInput
from .models import *
from users.forms import *
from users.models import *


from django import forms


class DateInput(forms.DateInput):
    input_type = 'date'


class Employee_CVForm(ModelForm):
    class Meta:
        model = Employee_CV
        fields = '__all__'
        exclude = ['p_user','meet_link_sent','cv']

        labels = {
            'country':'Choose Country',          
            'interestedfor':'Interested For', 
            'fullname':'Full Name', 
            'phonenumber':'Contact Number', 
            'dateofbirth':'Date of Birth', 
            'education':'Highest Education',  
            'nationalid':'National ID',              
            'startingdate':'Earliest Start Date', 

            'position':'Position',  
            'shifttime':'Shift Time',           
            'cv':'CV (pdf only) *', 
            'agreementlicens':'By registering and submitting with IIMI, you accept our License Agreements, Privacy Policy and Terms of use, and agree to receive emails, text or phone calls.',    

            }
        widgets = {'startingdate': DateInput(attrs={'type': 'date'}),
                   'dateofbirth': DateInput(attrs={'type': 'date'}),
                   }
     
               
    def __init__(self, *args, **kwargs):
        super(Employee_CVForm,self).__init__(*args, **kwargs)
        
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})
        self.fields['agreementlicens'].widget = CheckboxInput(attrs={'class': 'form-check-input'})
        




class Documents_upload_form(ModelForm):
    class Meta:
        model = Documents_upload
        fields = '__all__'
        exclude = ['p_user']

        labels = {
            'nid_birthcertificate':'NID / Birth Certificate',          
            'education_certificate':'Highest Education Certificate', 
            'chairman_certificate':'Chairman / Word Commisonner Certificate', 
            'testimonial':'Testimonial', 
      

            }
        # widgets = {'startingdate': DateInput(attrs={'type': 'date'}),
        #            'dateofbirth': DateInput(attrs={'type': 'date'}),
        #            }
     
               
    def __init__(self, *args, **kwargs):
        super(Documents_upload_form,self).__init__(*args, **kwargs)
        
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})
        # self.fields['agreementlicens'].widget = CheckboxInput(attrs={'class': 'form-check-input'})
        







































# class JobProfleForm(ModelForm):
#     class Meta:
#         model = Employee_profile
#         fields = '__all__'
#         exclude = ['user', 'u_user', 'has_used_secret_key']
#         labels = {
#             'name': 'Full Name',
#             'email': 'Contact Email',
#             'phone': 'Contact Number',
#             'profile_pic': 'Profile Picture',
#             'nid': 'National ID Number',
#             'bank_account': 'Bank Account Number',
#             'dob': 'Date of Birth',
#             'license': 'License Aggrement',
#         }
#         widgets = {
#             'dob': DateInput(),
#             'profile_pic': FileInput(attrs={'class': 'form-control', 'input_type': 'file'}),
#         }

#     education_degree = forms.ChoiceField(choices=Employee_profile.Education, widget=forms.Select(attrs={'class': 'form-control'}))
#     working_hours = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
#     have_computer = forms.ChoiceField(choices=Employee_profile.Computer, widget=forms.Select(attrs={'class': 'form-control'}))
#     comment = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4}))
#     license = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))

#     def __init__(self, *args, **kwargs):
#         super(JobProfleForm, self).__init__(*args, **kwargs)

#         for name, field in self.fields.items():
#             field.widget.attrs.update({'class': 'form-control'})

#         self.fields['license'].widget = CheckboxInput(attrs={'class': 'form-check-input'})
