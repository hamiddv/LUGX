from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.contrib.auth.forms import UserCreationForm
from .models import User

numeric_validator = RegexValidator(r'^[0-9]*$', 'only number')


class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if (
                email
                and self._meta.model.objects.filter(email__iexact=email).exists()
        ):
            self._update_errors(
                ValidationError(
                    {
                        "email": self.instance.unique_error_message(
                            self._meta.model, ["email"]
                        )
                    }
                )
            )
        else:
            return email

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


class ForgetPasswordForm(forms.ModelForm):
    error_messages = {
        "email": "a user with that email does not exist"
    }
    email = forms.EmailField(required=True)

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if (
                email
                and not self._meta.model.objects.filter(email__iexact=email).exists()
        ):
            self._update_errors(ValidationError({"email": self.error_messages["email"]}))
        else:
            return email

    class Meta:
        model = User
        fields = ["email"]


class ForgetPasswordConfirmForm(forms.Form):
    email = forms.EmailField(required=True)
    code1 = forms.CharField(max_length=1, validators=[numeric_validator])
    code2 = forms.CharField(max_length=1, validators=[numeric_validator])
    code3 = forms.CharField(max_length=1, validators=[numeric_validator])
    code4 = forms.CharField(max_length=1, validators=[numeric_validator])
