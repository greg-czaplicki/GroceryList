from django.views.generic import ListView

from groceries.models import *


# Create your views here.
class HomeTemplateView(ListView):
    template_name = 'Index.html'
    model = Item
