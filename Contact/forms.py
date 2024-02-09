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
        labels = {
            "name": "Name",
            "email": "Email",
            "phone_number": "Phone Number",
            "address": "Address",
        }
        labels_attrs = {
            "name": {"class": "label_style"},  
            "email": {"class": "label_style"},
            "phone_number": {"class": "label_style"},
            "address": {"class": "label_style"},
        }