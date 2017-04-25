import operator

from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import DeleteView

from groceries.models import *


def Home(request):
    if request.method == 'POST':
        print('*' * 200)
        print(request.POST)
        print('*' * 200)
        name = request.POST.get('name')
        name = name.title()
        category = request.POST.get('category')
        quantity = request.POST.get('quantity')
        weight = request.POST.get('weight')

        if quantity:
            quantity = quantity
        else:
            quantity = 1

        if weight:
            weight = weight
        else:
            weight = 0

        search = Item.objects.filter(name=name)

        if search:
            update = Item.objects.get(name=name)
            add_quant = quantity
            update.quantity += int(add_quant)
            add_weight = weight
            update.weight += int(add_weight)
            update.save()
        else:
            item = Item.objects.create(
                name=name.title(),
                category=category,
                quantity=quantity,
                weight=weight
            )
            item.save()

        return HttpResponseRedirect('')

    else:
        results = Item.objects.all()
        item_order = sorted(results, key=operator.attrgetter('name'))
        ordered = sorted(item_order, key=operator.attrgetter('category'))
        return render(request, 'Index.html', {'results': ordered})


def DeleteAll(request):
    entire_db = Item.objects.all()
    entire_db.delete()
    return redirect(Home)