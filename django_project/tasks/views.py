from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse 



#This class will represent the form
class NewTaskForm(forms.Form):
    #The input textbox will only take characters
    task = forms.CharField(label="New Task")
    #The input textbox will only take Integers
    priority = forms.IntegerField(label="Priority", min_value=1, max_value=10)
# Create your views here.
def index(request):
    #Check if there already a list of tasks in the request session
    if "tasks" not in request.session:
        #if tasks list is not in the session, then I would like to crate a tasks list to the request.session 
        request.session["tasks"] = []
    return render(request, "tasks/index.html", {
        "tasks": request.session["tasks"]
    })

def add(request):
    #Check which request method is being used
    #Server side validation
    if request.method == "POST":
        #Process the results of that request 
        #request.POST contains all of the data that the user submitted when they submitted the form
        form = NewTaskForm(request.POST)
        #Check if the form is valid
        if form.is_valid():
            #If it is then we take the data from the form and get the task and save it in the task variable
            #Then add it to my list of task
            task = form.cleaned_data["task"]
            #tasks.append(task) Instead of using this to add a new task to the list 
            request.session["tasks"] += [task]
            #Make sure to import HttpResponseRedirect and reverse when using it 
            return HttpResponseRedirect(reverse("tasks:index"))
        else:
            #If the form is not vaild then return the add.html file 
            #But instead of providing a new form back to them just send back the existing form data, 
            #So it can show the user the error
            return render(request, "tasks/add.html", {
                "form": form

            })
    #If the user only tried to get the page rather than submitting a form then just render an empty form
    return render(request, "tasks/add.html", {
        "form": NewTaskForm()
    })