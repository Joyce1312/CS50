#imports thr class httpResponse
from django.http import HttpResponse
from django.shortcuts import render 

# Create your views here.
def index(request):
    return render(request, "testing/index.html")

def joyce(request):
    return HttpResponse("Hello, Joyce!")

def lucy(request):
    return HttpResponse("Hello, Lucy!")
#Says hello whoever's name is given
#The .capitalize will help capitalized the first letter
#def greet(request, name):
    #return HttpResponse(f"Hello, {name.capitalize()}!")
#This function says hello whoever's name is given using HTML
#The third argument is called the context
#Context is all of the information that we want to provide to the template (variables)
def greetings(request, name):
    return render(request, "testing/greet.html", {
        "name": name.capitalize()
    })