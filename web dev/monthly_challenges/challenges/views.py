from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect


monthly_challenges = {
    "january": "Eat No Meat For The Entire Month.",
    "february": "Go For A Morning Run Everyday Of The Month.",
    "march": "Refrain From Eating Junk Food This Whole Month.",
    "april": "Learn Programming",
    "may": "Eat No Meat For The Entire Month.",
    "june": "Go For A Morning Run Everyday Of The Month.",
    "july": "Refrain From Eating Junk Food This Whole Month.",
    "august": "Learn Programming",
    "september": "Eat No Meat For The Entire Month.",
    "october": "Go For A Morning Run Everyday Of The Month.",
    "november": "Refrain From Eating Junk Food This Whole Month.",
    "december": "Learn Programming",
}

def monthly_challenge_by_number(request, month):
    # return HttpResponse(month)
    months = list(monthly_challenges.keys())
    
    if month > len(months):
        return HttpResponseNotFound("Invalid Month")
    
    redirect_month = months[month - 1]
    return HttpResponseRedirect('/challenges/' + redirect_month)
# Create your views here.
# def january(request):
#     return HttpResponse("Eat No Meat For The Entire Month.")

# def february(request):
#     return HttpResponse("Go For A Morning Run Everyday Of The Month.")

# def march(request):
#     return HttpResponse("Refrain From Eating Junk Food This Whole Month.")

# def april(request):
#     return HttpResponse("Learn Programming")

# def monthly_challenge(request, month):
    # challenge_text = None
    # if month == 'january':
    #     challenge_text = "Eat No Meat For The Entire Month."
    # elif month == 'february':
    #     challenge_text = "Go For A Morning Run Everyday Of The Month."
    # elif month == 'march':
    #     challenge_text = "Refrain From Eating Junk Food This Whole Month."
    # elif month == 'april':
    #     challenge_text = "Learn Programming"
    # else:
    #     return HttpResponseNotFound("That Month Is Not Supported!")
    # return HttpResponse(challenge_text)
    
    
def monthly_challenge(request, month):
    try:
        challenge_text= monthly_challenges[month]
        return HttpResponse(challenge_text)
    except:
        return HttpResponseNotFound("That Month Is Not Supported.")
