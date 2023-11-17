from django.urls import path

from user.views import SignUpView, UserProfileDetailView, UserProfileUpdateView

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path("profile/", UserProfileDetailView.as_view(), name="profile"),
    path("profile/update/", UserProfileUpdateView.as_view(), name="profile-update"),
]

app_name = "user"
