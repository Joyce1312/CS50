"""django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
#This file is the urls.py file for the entire project
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/',admin.site.urls),
    #First argument helps lead to the testing application
    #Second argument is saying that after you included the testing path, 
    #then include all the urls from the urls.py of the testing application
    #If you use include then you also have to import include
    path('testing/', include("testing.urls")),
    path('newyear/', include("newyear.urls")),
    path('tasks/', include("tasks.urls")),
]
