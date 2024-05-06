from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import breakfast_details,dinner_details,juice_details,lunch_details,sweet_details
from django.db.models import Q
from .models import *


# Create your views here.
def home(request):
    return render(request,"homepage.html")

def recipe_details(request):
    return render(request,"recipe_details.html")

def breakfast_recipe(request):
    query = request.GET.get('search')
    obj = breakfast_details.objects.all()

    if query:
        obj = obj.filter(Q(title__icontains=query))

    return render(request, "breakfast.html", {'image': obj})

def breakfast_detail(request,id):
    obj=get_object_or_404(breakfast_details, id=id)
    return render(request,'recipe_details.html',{"image":obj})


def dinner_recipe(request):
    query = request.GET.get('search')
    obj = dinner_details.objects.all()

    if query:
        obj = obj.filter(Q(title__icontains=query))

    return render(request, "dinner.html", {'image': obj})

def dinner_detail(request,id):
    obj=get_object_or_404(dinner_details, id=id)
    return render(request,'recipe_details.html',{"image":obj})


def juice_recipe(request):
    query = request.GET.get('search')
    obj = juice_details.objects.all()

    if query:
        obj = obj.filter(Q(title__icontains=query))

    return render(request, "juice.html", {'image': obj})

def juice_detail(request,id):
    obj=get_object_or_404(juice_details, id=id)
    return render(request,'recipe_details.html',{"image":obj})

#lunch recipe

def lunch_recipe(request):
    query = request.GET.get('search')
    obj = lunch_details.objects.all()

    if query:
        obj = obj.filter(Q(title__icontains=query))

    return render(request, "lunch.html", {'image': obj})

def lunch_detail(request,id):
    obj=get_object_or_404(lunch_details, id=id)
    return render(request,'recipe_details.html',{"image":obj})


#sweet recipe

def sweet_recipe(request):
    query = request.GET.get('search')
    obj = sweet_details.objects.all()

    if query:
        obj = obj.filter(Q(title__icontains=query))

    return render(request, "sweet.html", {'image': obj})

def sweet_detail(request,id):
    obj=get_object_or_404(sweet_details, id=id)
    return render(request,'recipe_details.html',{"image":obj})




