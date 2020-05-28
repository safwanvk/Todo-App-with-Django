from django.shortcuts import render

# Create your views here.
def home(request):

    return render(request, 'home.html')

def update(request):

     return render(request, 'update.html')