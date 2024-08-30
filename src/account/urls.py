from django.urls import path
from account.views import (
    UserRegisterView,
    UserLoginView,
    UserLogoutView,
    ProfileView,
    sites_view,
    site_details,
    create_site,
)

app_name = "account"

urlpatterns = [
    path("register/", UserRegisterView.as_view(), name="register"),
    path("login/", UserLoginView.as_view(), name="login"),
    path("logout/", UserLogoutView.as_view(), name="logout"),
    path("profile/", ProfileView.as_view(), name="profile"),
    path("sites/", sites_view, name="sites"),
    path("add-site/", create_site, name="add-site"),
    path("site/<pk>/", site_details, name="site-details"),
]
