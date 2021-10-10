from django.shortcuts import render
from django.http import HttpResponse
from home.models import Contact
from datetime import datetime
from django.contrib import messages

# Create your views here.
def home(request):
    # return HttpResponse('Welcome! to the world of programming.') # only for string
    context = {
        "name": "Python",
        "designation": "Software Developer"
    }
    # messages.success(request, "Test message!!!!")
    return render(request, 'index.html', context)


def about(request):
    return HttpResponse('About Page')


def services(request):
    return HttpResponse('services Page')


def contact(request):
    if request.method == "POST":
        number = request.POST.get("number")
        email = request.POST.get("email")
        msg = request.POST.get("message")
        date = datetime.today()

        # create object for class  i.e model
        contact = Contact(number=number, email=email, message=msg, date=date)
        contact.save()
        messages.success(request, "Submitted Successfully!")

    return render(request, "contact_us.html")
