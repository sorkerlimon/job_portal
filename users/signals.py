from django.db.models.signals import post_save
from django.contrib.auth.models import User
from .models import Employee_profile
from django.contrib.auth.models import Group

# def customer_profile(sender,instance,created, **kwargs):
#     if created:
#             group = Group.objects.get(name='employee')
#             instance.groups.add(group)
#             Employee_profile.objects.create(user=instance,name=instance.username)

# post_save.connect(customer_profile,sender=User)

def customer_profile(sender, instance, created, **kwargs):
    if created:
        group = Group.objects.get(name='employee')
        instance.groups.add(group)

        # Delete existing Employee_profile objects for the user
        Employee_profile.objects.filter(user=instance).delete()

        # Create new Employee_profile object
        Employee_profile.objects.create(
            user=instance,
            name=instance.username,
            phone=instance.phone,
            email=instance.email,
        )

post_save.connect(customer_profile, sender=User)

