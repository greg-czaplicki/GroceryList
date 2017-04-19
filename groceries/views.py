from django.shortcuts import render

from groceries.models import *


# Create your views here.
def Index(request):
    paper = Paper_Plastic.objects.all()
    paper_name = Paper_Plastic.get_cname(paper)

    snacks = Snacks.objects.all()
    snacks_name = Snacks.get_cname(snacks)
    return render(request, 'Index.html', {'snacks': snacks,
                                          'snacks_name': snacks_name,
                                          'paper': paper,
                                          'paper_name': paper_name})
