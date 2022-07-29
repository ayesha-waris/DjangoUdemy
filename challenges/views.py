from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.http import HttpResponse
from django.urls import reverse
from django.template.loader import render_to_string


monthly_challenges = {
    "january": "Eat no meat for the entire month!",
    "february": "Walk for at least 20 minutes every day!",
    "march": "Learn Django for at least 20 minutes every day!",
    "april": "Eat no meat for the entire month!",
    "may": "Walk for at least 20 minutes every day!",
    "june": "Learn Django for at least 20 minutes every day!",
    "july": "Eat no meat for the entire month!",
    "august": "Walk for at least 20 minutes every day!",
    "september": "Learn Django for at least 20 minutes every day!",
    "october": "Eat no meat for the entire month!",
    "november": "Walk for at least 20 minutes every day!",
    "december": None
}


def index(request):
    list_items = ""
    months = list(monthly_challenges.keys())

      
    
    return render(request, 'challenges/index.html',{
      "months": months
    })


def months(request, month):
    return render(request, 'challenges/challenge.html', {
        "text": month
    })
    # response_data = render_to_string('challenges/challenge.html')
    # return HttpResponse(response_data)


def months_number(request, month):

    redirect_path = reverse("month", args=["month"])  # /challenges/month
    return HttpResponseRedirect(redirect_path)
