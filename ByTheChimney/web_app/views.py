from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse

from .models import Product


def index(request):
    #events = get_object_or_404(Event.getUpcoming())

    #return render(request, 'polls/index.html', {'events': events})
    return render(request, 'web_app/index.html')

def store(request):
    return render(request, 'web_app/store.html')

def about(reuqest):
    return render(request, 'web_app/about.html')