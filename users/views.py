import random

from django.contrib import messages
from django.http import HttpResponseRedirect
from django.views import View
from django.views.generic import FormView
from django.contrib.auth import login, logout

from .models import User, UserConfirmCode
from .forms import *


class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect("/")


class SignUpView(FormView):
    template_name = "registration/sign-up.html"
    form_class = SignUpForm
    success_url = "/"

    def form_valid(self, form):
        username = form.cleaned_data["username"]
        email = form.cleaned_data["email"]
        password1 = form.cleaned_data["password1"]
        password2 = form.cleaned_data["password2"]
        if User.objects.filter(username=username).exists():
            messages.error(self.request, "username already taken")

        elif User.objects.filter(email=email).exists():
            messages.error(self.request, "email already taken")

        else:
            user = User.objects.create_user(username, email, password=password1)
            user.save()
            login(self.request, user)
            return super().form_valid(form)

        return HttpResponseRedirect("/sign-up/")


class ForgetPasswordView(FormView):
    template_name = "registration/forget-password.html"
    form_class = ForgetPasswordForm
    success_url = "/forget-password-confirm/"

    def get_success_url(self):
        return f"/forget-password-confirm/?email={self.get_form().data['email']}"

    def form_valid(self, form):
        email = form.cleaned_data["email"]
        user = User.objects.get(email=email)
        if UserConfirmCode.objects.all().filter(user=user).exists():
            confirm_code = UserConfirmCode.objects.get(user=user)
            confirm_code.confirm_code = str(random.randint(1000, 9999))

            confirm_code.save()
            return super().form_valid(form)

        else:
            confirm_code = UserConfirmCode.objects.create(
                user=user, confirm_code=str(random.randint(1000, 9999))
            )
            confirm_code.save()

            return super().form_valid(form)


class ForgetPasswordConfirmView(FormView):
    template_name = "registration/forget-password-confirm.html"
    form_class = ForgetPasswordConfirmForm
    success_url = "/"

    def form_valid(self, form):
        email = form.cleaned_data["email"]

        code1 = form.cleaned_data["code1"]
        code2 = form.cleaned_data["code2"]
        code3 = form.cleaned_data["code3"]
        code4 = form.cleaned_data["code4"]

        code = code1 + code2 + code3 + code4
        try:
            user = User.objects.all().filter(email=email)[0]
            confirm_code = UserConfirmCode.objects.get(user=user)
            print(confirm_code.confirm_code)
            if confirm_code.confirm_code == code:
                login(self.request, user)
                return super().form_valid(form)

            messages.error(self.request, "code is not valid")
            return HttpResponseRedirect(f"/forget-password-confirm/?email={email}")

        except:
            messages.error(self.request, "somthing went wrong")
            return HttpResponseRedirect(f"/forget-password-confirm/?email={email}")

