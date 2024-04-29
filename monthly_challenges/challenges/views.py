from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect,Http404
from django.urls import reverse 

# challenges dictionary 
monthly_challenges = {
    "january": "eat no meat for the entire month",
    "february": "learn django 30 minutes everyday", 
    "march": "walk for at least 1 hour daily",
    "april": None,
    "may": "eat no meat for the entire month",
    "june": "learn django 30 minutes everyday", 
    "july": "walk for at least 1 hour daily",
    "august": "learn python programming 1 hour everyday",
    "september": "eat no meat for the entire month",
    "october": "learn django 30 minutes everyday", 
    "november": None,
    "december": "learn python programming 1 hour everyday",
}

# Create your views here.
def index(request):
    # list_items = ""
    months = list(monthly_challenges.keys())
    # for month in months:
    #     capitalized_month = month.capitalize()
    #     month_path = reverse('month-challenge', args=[month])
    #     list_items += f"<li><a href='{month_path}'>{capitalized_month}</a></li>"
    # response_data = f"<ul>{list_items}</ul>" 
    # return HttpResponse(response_data)
    return render(request, 'challenges/index.html', {
        "months": months 
    })

def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("Invalid Month")
    redirect_month = months[month - 1]
    redirect_path = reverse("month-challenge", args=[redirect_month]) 
    # return HttpResponseRedirect("/challenges/" + redirect_month)
    return HttpResponseRedirect(redirect_path)

def monthly_challenge(request, month): 
    try:
        challenge_text = monthly_challenges[month]
        return render(request, 'challenges/challenge.html', {
            'challenge': challenge_text,
            'month': month 
        })
        # challenge_text = monthly_challenges[month]
        # return HttpResponse(challenge_text)
    except:
        raise Http404() 
        # return HttpResponseNotFound("That month is not supported!") 
