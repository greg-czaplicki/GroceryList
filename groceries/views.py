import json
import operator

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect

from groceries.models import *




def Home(request):
    if request.method == 'POST':
        print('*'*200)
        print(request.POST)
        print('*'*200)
        name = request.POST.get('name')
        category = request.POST.get('category')
        quantity = request.POST.get('quantity')
        weight = request.POST.get('weight')

        newItem = Item.objects.create(
            name = name,
            category = category,
            quantity = str(quantity),
            weight = str(weight),
        )
        newItem.save()
        return HttpResponseRedirect('/')
    else:
        results = Item.objects.all()
        item_order = sorted(results, key=operator.attrgetter('name'))
        ordered = sorted(item_order, key=operator.attrgetter('category'))
        return render(request, 'Index.html', {'results': ordered})
