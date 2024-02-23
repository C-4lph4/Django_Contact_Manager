from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = "__all__"
        widgets = {
            "picture":forms.ClearableFileInput(attrs={"class": "form_style file_input"}),
            "name": forms.TextInput(attrs={"class": "form_style"}),
            "email": forms.TextInput(attrs={"class": "form_style"}),
            "phone_number": forms.TextInput(attrs={"class": "form_style"}),
            "address": forms.TextInput(attrs={"class": "form_style"}),
        }
        labels = {
            "picture":"Picture",
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