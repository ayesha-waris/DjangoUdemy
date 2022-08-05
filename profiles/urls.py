from django.urls import path

from . import views

urlpatterns = [
    path("profiles", views.CreateProfileView.as_view()),
    path("user-profiles",views.ProfilesView.as_view()),
] 