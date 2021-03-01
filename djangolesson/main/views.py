from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    data = {
        'title': 'Главная страница!',
        'values' : ['sdf', '121', 'sdfs'],
        'obj' : {
            'car': 'BMW',
            'age': 18,
            'hobby': 'football'
        }
    }
    return render(request,'main/index.html',data)

def about(request):
    return HttpResponse("<h4>О нас</h4>")
