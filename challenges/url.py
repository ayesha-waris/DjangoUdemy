from django.urls import path
from . import views


urlpatterns = [
    
    path('<int:month>', views.months_number),
    path('<str:month>', views.months)
]
