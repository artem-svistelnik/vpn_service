from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView, LogoutView
from account.forms import CustomUserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import UpdateView

from account.forms import SiteForm
from account.forms import UserEditForm
from django.contrib.auth import get_user_model
from django.shortcuts import render

from service.models import Site

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


@login_required
def sites_view(request):
    sites = Site.objects.filter(user_id=request.user.id)
    return render(request, "statistic/sites.html", {"sites": sites})


@login_required
def create_site(request):
    if request.method == "POST":
        form = SiteForm(request.POST)
        if form.is_valid():
            site = form.save(commit=False)
            site.user = request.user
            site.save()
            return redirect("account:site-details", pk=site.id)
    else:
        form = SiteForm()

    return render(request, "statistic/create_site.html", {"form": form})


@login_required
def site_details(request, pk: int):
    site = Site.objects.filter(id=pk).first()
    if request.method == "POST":
        form = SiteForm(request.POST, instance=site)
        if form.is_valid():
            form.save()
            return redirect("account:site-details", pk=site.id)
    else:
        form = SiteForm(instance=site)
    return render(request, "statistic/site_details.html", {"site": site})
