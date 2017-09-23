from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse
from django.core.validators import RegexValidator

# Create your models here.
class CRUD(models.Model):
    first_name = models.CharField(max_length=30,blank=False, null=False)
    last_name = models.CharField(max_length=30,blank=False, null=False)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    telephone = models.CharField(validators=[phone_regex], max_length=15,blank=False, null=False)
    date_of_contact = models.DateField(auto_now=False,auto_now_add=False)

    def __str__(self):
        return self.first_name + self.last_name