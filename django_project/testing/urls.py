#To create a URL you need to first import from django.urls import path
from django.urls import path
#Import views.py from current directory (folder)
#The period means from current directory
from . import views
#A list of all the allowable URLs that can be accessed for this particular app
urlpatterns = [
    #The double quotes means no additional arguments (Meaning nothing at the end of the route)
    #The second part of the path is what view is rendered when the url is visited
    path("",views.index,name="index"),
    #The string in the double quote is what you type in the url to load the function
    path("joyce",views.joyce,name="joyce"),
    path("lucy",views.lucy,name="lucy"),
    #The first argumant is saying that this route can be any string
    #path("<str:name>", views.greet, name="greet"),
    path("<str:name>", views.greetings, name="greetings")
]