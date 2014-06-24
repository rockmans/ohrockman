from django.http import HttpResponse, Http404
from django.shortcuts import get_object_or_404, render_to_response, render
from django.shortcuts import render

from familytree.models import FamilyMember, Marriage


def index(request):
    oscar = get_object_or_404(FamilyMember, pk=1)
    helen = get_object_or_404(FamilyMember, pk=13)    
    return render(request, 'index.html', {'oscar':oscar, 'helen':helen})

def maintainence(request):
    return render(request, 'maintainence.html', {})

def family_member(request, member_id):
    person = get_object_or_404(FamilyMember, pk=member_id)
    marriages = Marriage.objects.marriage_with(person)
    return render_to_response('member_info.html', {'person':person, 'marriages':marriages})

def family_member_search(request):
    first = request.GET.get('first',None)
    middle = request.GET.get('middle',None)
    last = request.GET.get('last',None)
    maiden = request.GET.get('maiden',None)
    person_list = FamilyMember.objects.search_members(first, middle, last, maiden)
    if not person_list:
        raise Http404
        #return HttpResponse('Search Fields were %s - %s - %s - %s'%(first_name, middle_name, last_name, maiden_name)) 
    return render_to_response('member_list.html', {'person_list':person_list})