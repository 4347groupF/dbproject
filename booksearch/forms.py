from django import forms
from django.core.exceptions import ValidationError

from .models import Borrower

def validate_ssn(ssn):
    if Borrower.objects.get(ssn=ssn) is None:
        return
    
    raise ValidationError("An account is already associated with this SSN.")

class SignUpForm(forms.Form):
    first_name = forms.CharField(min_length=1, max_length=50, required=True)
    last_name = forms.CharField(min_length=1, max_length=50, required=True)
    ssn = forms.CharField(min_length=9, max_length=12, required=True, validators=[validate_ssn])
    phone = forms.CharField(min_length=10, max_length=14, required=True)
    address = forms.CharField(min_length=1, max_length=100, required=True)
    state = forms.CharField(min_length=1, max_length=15, required=True)
    city = forms.CharField(min_length=1, max_length=100, required=True)
    email = forms.EmailField(min_length=3, max_length=100, required=True)