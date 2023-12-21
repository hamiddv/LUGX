from django.urls import path
from django.contrib.auth.views import LoginView

from .views import *

urlpatterns = [
    path("sign-up/", SignUpView.as_view()),
    path("login/", LoginView.as_view()),
    path("logout/", LogoutView.as_view()),
    path("forget-password/", ForgetPasswordView.as_view()),
    path("forget-password-confirm/", ForgetPasswordConfirmView.as_view())
]
