from django.shortcuts import render

def index(request):
    return render(request, 'index.html', {})

def maintainence(request):
    return render(request, 'maintainence.html', {})