from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate , login as loginUser , logout
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm

from app1.forms import TaskForm
from app1.models import Task
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def home(request):
    if request.user.is_authenticated:
        user = request.user
        form = TaskForm()
        tasks = Task.objects.filter(user = user).order_by('priority')
        return render(request, 'index.html' , context={'form' : form , 'tasks' : tasks})

def login(request):
    if request.method ==  'GET':
        form = AuthenticationForm()
        context = {
        "form" : form
        }
        return render(request, 'login.html' , context=context)
    else:
        form = AuthenticationForm(data = request.POST)
        print(form.is_valid())
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username = username , password = password)
            if user is not None:
                loginUser(request , user )
                return redirect('home')    
        else:
            context = {
            "form" : form
            }
            return render(request, 'login.html' , context=context)


def signup(request):
    if request.method == 'GET':
        form = UserCreationForm()
        context = {
        "form" : form
        }
        return render(request, 'signup.html' , context=context)
    else:
        print(request.POST)
        form = UserCreationForm(request.POST)
        context = {
        "form" : form
        }
        if form.is_valid():
            user = form.save()
            print(user)
            if user is not None:
                return redirect('login')
        else:
           return render(request, 'signup.html' , context=context) 
            

@login_required(login_url='login')
def add_Task(request):
    if request.user.is_authenticated:
        user = request.user
        form = TaskForm(request.POST)
        if form.is_valid():
           print(form.cleaned_data)
           task = form.save(commit=False)
           task.user = user
           task.save()
           return redirect("home")
        else:
           return render(request, 'index.html' , context={'form' : form})
 

def delete_task(request , id):
    print(id)
    Task.objects.get(pk = id).delete()
    return redirect('home')

def change_task(request , id , status):
    task = Task.objects.get(pk = id)
    task.status = status
    task.save()
    return redirect('home')


@login_required(login_url='login')
def signout(request):
    logout(request)
    return redirect('login')



