from django.urls import path, include
from . import views


urlpatterns = [
  path("", views.listing, name="listing"),
  path("view_blog/<int:blog_id>/", views.view_blog, name="view_blog"),
  path("see_request/", views.see_request),
  path("user_info/", views.user_info),
  path("private_place/", views.private_place),
  path("accounts/", include("django.contrib.auth.urls")),
  path("dashboard/", views.dashboard, name="dashboard"),
]
  
