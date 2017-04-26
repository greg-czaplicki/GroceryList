import operator
from decimal import Decimal

from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

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

        if not name.strip():
            messages.warning(request, "Item must have a name!")
            return HttpResponseRedirect(request.path)

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
            update.weight += Decimal(add_weight)
            update.save()
        else:
            item = Item.objects.create(
                name=name,
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


def Completed(request, itemname):
    item = Item.objects.get(name=itemname)

    if item.is_complete == False:
        item.is_complete = True
    else:
        item.is_complete = False

    item.save()
    return redirect(Home)
