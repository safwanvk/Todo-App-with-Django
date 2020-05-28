from django.shortcuts import render, redirect

# Create your views here.
import todo
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


def update(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    form = TodoForm(instance=todo)
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('home')

    return render(request, 'update.html', {'form': form, 'todo': todo})
