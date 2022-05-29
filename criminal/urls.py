from django.contrib import admin
from django.urls import path
from .views import home, camera

urlpatterns = [
    path('',home, name='home'),
    path('camera',camera, name='camera'),

]