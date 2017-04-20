import operator

from django.shortcuts import render

from groceries.models import *


def Home(request):
    results = Item.objects.all()
    item_order = sorted(results, key=operator.attrgetter('name'))
    ordered = sorted(item_order, key=operator.attrgetter('category'))
    return render(request, 'Index.html', {'results': ordered})
