from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import RequestContext, loader

from familytree.models import FamilyMember

def tree(request, member_id=None):
    family_head = get_object_or_404(FamilyMember, pk=member_id or 1)

    template = loader.get_template('tree_vertical.html')
    context = RequestContext(request, {"family_head": family_head})
    return HttpResponse(template.render(context))
