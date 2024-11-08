from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User
from .models import *
context = ""
def home(request):
    for p in PeopleAddress.objects.all()[0:5]:
        context+= p.address
        print(p.address)
    
    return render(request,"home.html",{"context":context})