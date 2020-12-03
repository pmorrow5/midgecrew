from django.shortcuts import render
import datetime
from dateutil.relativedelta import relativedelta
# Create your views here.

posts = [
    {
        'author': 'CoreyMS',
        'title': 'Post 1',
        'content': 'First Post Content',
        'date_posted': 'August 27, 2018'
    },
    {
        'author': 'Jane',
        'title': 'Post 2',
        'content': 'Second Post Content',
        'date_posted': 'August 29, 2018'
    }
]

def home(request):
    context = {
        'title': "Countdown to Okoboji",
    }

    return render(request, "okoboji/home.html", context)


def about(request):
    return render(request, "okoboji/about.html")
