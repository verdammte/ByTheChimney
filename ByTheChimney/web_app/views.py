from django.shortcuts import get_object_or_404, render


def index(request):
    return render(request, 'polls/index.html')

def store(request):
    return render(request, 'polls/store.html')

def about(reuqest):
    return render(request, 'polls/about.html')