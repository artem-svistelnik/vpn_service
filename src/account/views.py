from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView, LogoutView
from account.forms import CustomUserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import UpdateView
from account.forms import UserEditForm
from django.contrib.auth import get_user_model
from django.shortcuts import render

User = get_user_model()


def index(request):
    return render(request, "index.html")


class UserRegisterView(CreateView):
    form_class = CustomUserCreationForm
    model = User
    template_name = "account/register.html"
    success_url = reverse_lazy("account:login")


class UserLoginView(LoginView):
    template_name = "account/login.html"


class UserLogoutView(LogoutView):
    next_page = reverse_lazy("account:login")


class ProfileView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserEditForm
    template_name = "account/profile.html"
    success_url = reverse_lazy("account:profile")

    def get_object(self, queryset=None):
        return self.request.user
