from django import forms

from .models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ["name", "surname", "subject", "email", "message"]
        widgets = {
            "name": forms.TextInput(
                    attrs={
                        "class": "contact-input form-control-lg rounded-pill form-control",
                        "placeholder": "Your Name...",
                    }
            ),
            "surname": forms.TextInput(
                attrs={
                    "class": "contact-input form-control-lg rounded-pill form-control",
                    "placeholder": "Your Surname..."
                }
            ),
            "subject": forms.TextInput(
                attrs={
                    "class": "contact-input form-control-lg rounded-pill form-control",
                    "placeholder": "Subject..."
                }
            ),
            "email": forms.EmailInput(
                attrs={
                    "class": "contact-input form-control-lg rounded-pill form-control",
                    "placeholder": "Your Email..."
                }
            ),
            "message": forms.Textarea(
                attrs={
                    "class": "form-control contact-input rounded-5 p-4",
                    "placeholder": "Your Massage...",
                    "rows": 4
                }
            )
        }
