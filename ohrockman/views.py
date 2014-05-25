from django.shortcuts import get_object_or_404
from django.shortcuts import render

from familytree.models import FamilyMember


def index(request):
    oscar = get_object_or_404(FamilyMember, pk=1)
    helen = get_object_or_404(FamilyMember, pk=13)    
    return render(request, 'index.html', {'oscar':oscar, 'helen':helen})

def maintainence(request):
    return render(request, 'maintainence.html', {})