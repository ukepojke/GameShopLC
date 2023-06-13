from django.shortcuts import render
from .models import *

def index(re):
    ps1 = Product.objects.get(id=1)
    product = Product.objects.all()[1:3]
    return render(re, 'index.html',{'product': product, 'ps1': ps1})

def about(re):
    return render(re, 'about.html')

def product(re):
    product = Product.objects.all()[1:]
    return render(re, 'product.html',{'product': product})

def video(re):
    product = Videogames.objects.all()
    return render(re, 'video.html',{'product': product})

def remot(re):
    return render(re, 'remot.html')

def contact(re):
    return render(re, 'contact.html')

def product_detail(re,id):
    product = Product.objects.get(id=id)
    return render(re,'product_detail.html',{'product':product})

def videogames_detail(re,id):
    videogames = Videogames.objects.get(id=id)
    return render(re,'videogames_detail.html',{'videogames':videogames})
