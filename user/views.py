from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import DetailView, UpdateView

from user.forms import UserCreateForm, UserUpdateForm
from user.models import User


class SignUpView(generic.CreateView):
    form_class = UserCreateForm
    template_name = "registration/signup.html"
    success_url = reverse_lazy("login")


class UserProfileDetailView(LoginRequiredMixin, DetailView):
    model = User
    template_name = "registration/profile.html"

    def get_object(self, queryset=None):
        return self.request.user


class UserProfileUpdateView(LoginRequiredMixin, UpdateView):
    form_class = UserUpdateForm
    template_name = "registration/profile_update.html"
    success_url = reverse_lazy("user:profile")

    def get_object(self, queryset=None):
        return self.request.user
