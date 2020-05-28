from django.shortcuts import render

# Create your views here.
from account.forms import TodoForm


def home(request):
    form = TodoForm()

    return render(request, 'home.html', {'form': form})


def update(request):
    return render(request, 'update.html')
