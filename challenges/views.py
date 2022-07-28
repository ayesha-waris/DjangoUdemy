from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.http import HttpResponse
from django.urls import reverse  
# Create your views here.


def months(request, month):
    return HttpResponse(month)

def months_number(request, month):
    redirect_path = reverse("month", args=["month"]); #/challenges/month
    return HttpResponseRedirect(redirect_path)