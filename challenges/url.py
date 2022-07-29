from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name = 'index'), # triggers /challenges/
    path('<int:month>', views.months_number),
    path('<str:month>', views.months, name="month")
]
