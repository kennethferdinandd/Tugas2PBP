from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required
from todolist.models import Task
from django.http import HttpResponseRedirect
from django.urls import reverse
from todolist.forms import TaskForm
from datetime import date


# Create your views here.
@login_required(login_url="/todolist/login")
def show_todolist(request) :
    todolist_items = Task.objects.filter(user=request.user)
    context = {
        "todolist" : todolist_items, 
        "username" : request.user
        }
    return render(request, "todolist.html", context)

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:login')
    
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('todolist:show_todolist')
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('todolist:login'))
    response.delete_cookie('last_login')
    return response

@login_required(login_url="/todolist/login")
def create_task(request) :
    form = TaskForm()
    if request.method == 'POST' :
        form = TaskForm(request.POST)
        if form.is_valid() :
            new_task = form.save(commit=False)
            new_task.user = request.user
            new_task.date = date.today()
            new_task.save()
           
        return HttpResponseRedirect(reverse("todolist:show_todolist"))
    context = {'form': form}
    return render(request, 'create-task.html', context)

@login_required(login_url="/todolist/login")
def delete_task (request, id):
    task = Task.objects.get(user=request.user, id=id)
    task.delete()
    return HttpResponseRedirect(reverse("todolist:show_todolist"))

def trigger_is_finished(request, id):
    task = Task.objects.get(user=request.user, id=id)
    task.is_finished = not(task.is_finished)
    task.save(update_fields = ['is_finished'])
    return HttpResponseRedirect(reverse("todolist:show_todolist"))