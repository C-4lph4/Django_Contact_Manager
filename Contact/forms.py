from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = "__all__"
        widgets = {
            "name": forms.TextInput(attrs={"class": "form_style"}),
            "email": forms.TextInput(attrs={"class": "form_style"}),
            "phone_number": forms.TextInput(attrs={"class": "form_style"}),
            "address": forms.TextInput(attrs={"class": "form_style"}),
        }