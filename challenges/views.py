from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string
# Create your views here. views can be functions or classes
monthly_challenges = {
    "january": "eat no meat",
    "february": "eat vegetables",
    "march": "have more fun",
    "april": "eat something good",
    "may": "walk daily",
    "june": "have more fun",
    "july": "boom baby",
    "august":"okay it's aug",
    "september": "dang birthday",
    "october": "okay lets see ",
    "november": "boom babyyy",
    "december": "okayyyy"
}

def chall_index(request):
    list_items = ""
    months = list(monthly_challenges.keys())
    

    for month in months:
        capitalized_month = month.capitalize()
        month_path = reverse("month-challenge", args=[month])
        list_items +=  f"<li><a href=\"{month_path}\">{capitalized_month}</a></li>"
        response_data = f"<ul>{list_items}</ul>"
    return HttpResponse(response_data)


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    
    if month < 0 or month > len(months):
        return HttpResponseNotFound("Please input a valid month")

    redirect_month = months[month-1]
    redirect_path = reverse("month-challenge",args=[redirect_month])  

    try:
        return HttpResponseRedirect(redirect_path)
    except:
        return HttpResponseNotFound("This month is not supported")


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        #response_data = f"<h1>{challenge_text}</h1>"
        response_data = render_to_string("challenges/challenge.html")
        return HttpResponse(response_data)
    except:
        return HttpResponseNotFound("<br> <h1>This month is not supported</h1>")

def challenge_list(request):

    return HttpResponse("<h1>months</h1>")
   