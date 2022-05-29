from django.contrib import admin
from django.urls import path
from .views import login, criminals

urlpatterns = [
    path('admin-login/',login, name='login'),
    path('criminal-page/',criminals, name='criminal-page')
]