from django import forms

class SignUpForm(forms.Form):
    first_name = forms.CharField(min_length=1, max_length=50, required=True)
    last_name = forms.CharField(min_length=1, max_length=50, required=True)
    ssn = forms.CharField(min_length=9, max_length=12, required=True)
    phone = forms.CharField(min_length=10, max_length=14, required=True)
    address = forms.CharField(min_length=1, max_length=100, required=True)
    state = forms.ChoiceField(choices=("TX", "AL"), required=True)
    city = forms.CharField(min_length=1, max_length=100, required=True)
    email = forms.EmailField(min_length=3, max_length=100, required=True)