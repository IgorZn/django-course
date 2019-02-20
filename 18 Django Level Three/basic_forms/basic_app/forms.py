from django import forms
from django.core import validators



class FormName(forms.Form):
    name = forms.CharField(label='Your name', max_length=100)
    email = forms.EmailField(label='Your email', max_length=100)
    bak_email = forms.EmailField(label='Your email again', max_length=100)
    text = forms.CharField(label='Your text', widget=forms.Textarea)

    def clean(self):
        all_clean = super().clean()
        email = all_clean['email']
        vmail = all_clean['bak_email']

        if email != vmail:
            raise forms.ValidationError("Emails do not match!")

