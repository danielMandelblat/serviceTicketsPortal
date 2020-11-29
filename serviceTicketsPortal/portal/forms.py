from django.forms import ModelForm
from django import forms

from portal.models import ticket

class ticket(ModelForm):
    class Meta:
        model = ticket
        fields = '__all__'
        exclude = ['id', 'created_date', 'changed_date', 'supporter']
        widgets = {'owner': forms.HiddenInput}

class new_ticket_form(ticket):
    super