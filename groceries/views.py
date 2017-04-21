import operator

from django.http import HttpResponseRedirect
from django.shortcuts import render

from groceries.models import *


def Home(request):
    if request.method == 'POST':
        print('*' * 200)
        print(request.POST)
        print('*' * 200)
        name = request.POST.get('name')
        category = request.POST.get('category')
        quantity = request.POST.get('quantity')
        weight = request.POST.get('weight')

        if quantity:
            quantity = quantity
        else:
            quantity = None

        if weight:
            weight = weight
        else:
            weight = None

        search = Item.objects.filter(name=name)

        if search:
            print('exists')
            update = Item.objects.get(name=name)
            update.quantity = 1
            update.quantity += 1
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
