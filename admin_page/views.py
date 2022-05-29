from django.shortcuts import render, redirect
import requests
from .models import Criminal
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required


def login(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            auth_login(request, user)
            return redirect('criminal-page')
        else:
            messages.success(request,f'username or password not correct!')

    return render(request,'admin_page/login.html')


@login_required
def criminals(request):
    criminal = Criminal.objects.all()
    p= Paginator(criminal, 5)
    page_number = request.GET.get('page')
    try:
        page_obj = p.get_page(page_number)  # returns the desired page object
    except PageNotAnInteger:
        # if page_number is not an integer then assign the first page
        page_obj = p.page(1)
    except EmptyPage:
        # if page is empty then return last page
        page_obj = p.page(p.num_pages)
    context = {'page_obj': page_obj}
    print(context['page_obj'])
    # sending the page object to index.html
    return render(request, 'admin_page/criminal-page.html', context)

def add_criminal(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        age = request.POST.get("age")
        sex = request.POST.get("sex")
        location= request.POST.get("location")
        image = request.POST.get("image")

        criminal = Criminal()
        criminal.name = name
        criminal.age = age
        criminal.sex = sex
        criminal.location = location
        criminal.image = image
        criminal.save()
    return redirect(request,)
