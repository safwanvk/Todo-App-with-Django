from django.shortcuts import render, redirect

# Create your views here.
from account.forms import TodoForm
from account.models import Todo


def home(request):
    form = TodoForm()
    todos = Todo.objects.all()
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    return render(request, 'home.html', {'form': form, 'todos': todos})


def update(request):
    return render(request, 'update.html')
