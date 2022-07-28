from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def months(request, month):
    return HttpResponse(month)

def months_number(request, month):
    return HttpResponseRedirect('/challenges/' + "month")