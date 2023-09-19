from django.contrib import admin
from django.urls import path,include
from .views import *
urlpatterns = [
    path('',list_cr_Persons.as_view()),
    path('<int:id>/',rud_Persons.as_view()),
]
