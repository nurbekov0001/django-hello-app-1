from django.shortcuts import render

def index_view(request):
    return render(request, 'home.html')


def index_1(request):
    return render(request, 'index_1.html')

def index_2(request):
    return render(request, 'index_2.html')

# Create your views here.
