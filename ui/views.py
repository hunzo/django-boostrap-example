from unicodedata import name
from django.shortcuts import render

# Create your views here.

def index(request):
    num = []
    for i in range(10):
        num.append(i)
    context = {
        "num": num
    }
    return render(request, 'index.html', context)
