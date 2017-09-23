from django import forms

from .models import CRUD

class CRUDForm(forms.ModelForm):

    date_of_contact = forms.DateTimeField(widget=forms.SelectDateWidget)

    class Meta:
        model = CRUD
        fields = ['first_name', 'last_name', 'telephone','date_of_contact']