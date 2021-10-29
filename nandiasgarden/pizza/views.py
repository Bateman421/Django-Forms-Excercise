from django.shortcuts import render
from .forms import PizzaForm

# Create your views here.


def home(request):
    return render(request, 'home.html')


def order(request):
    form = PizzaForm()
    return render(request, 'order.html', {'pizzaform': form})
