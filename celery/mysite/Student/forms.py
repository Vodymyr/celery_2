from django import forms

class SMSForm(forms.Form):
    phone_number = forms.CharField(max_length=20)
    message = forms.CharField(widget=forms.Textarea)
