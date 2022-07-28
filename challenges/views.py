from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.http import HttpResponse
from django.urls import reverse  
# Create your views here.


def months(request, month):
    response_data = f'<h1>{month}</h1>'
    return HttpResponse(response_data)

def months_number(request, month):
    
    redirect_path = reverse("month", args=["month"]); #/challenges/month
    return HttpResponseRedirect(redirect_path)