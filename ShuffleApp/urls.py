from django.contrib import admin
from django.urls import path
from ShuffleApp.views import home_page_view

urlpatterns = [

    path('', home_page_view)
    
]
