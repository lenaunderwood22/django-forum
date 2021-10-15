from django.urls import path

from .views import SignUpView
import accounts.views

urlpatterns = [
    path('signup/', SignUpView.as_view(), name="signup"),
    path('logout_redirect/', accounts.views.logout_redirect, name="logout_redirect"),
]
