from django.shortcuts import render, redirect
from django.http import HttpResponse
from todolist_app.models import TaskList
from todolist_app.forms import TaskForm
from django.contrib import messages
from django.core.paginator import Paginator


# Create your views here.
def todolist(request):
    if request.method == "POST":
        form = TaskForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request,("New Task added successfully!"))
        return redirect('todolist')
    else:
        all_tasks = TaskList.objects.all()
        paginater = Paginator(all_tasks,5)
        page = request.GET.get('pg')
        all_tasks = paginater.get_page(page)
       
        return render(request, 'todolist.html', {'all_tasks': all_tasks})

def contact(request):
    context = {
        'contact_text':"Welcome contact Page",
    }
    return render(request, 'contact.html',context)

def about(request):
    context = {
        'about_text':"Welcome about Page",
    }
    return render(request, 'about.html',context)
 

def delete_task(request, task_id):
    task = TaskList.objects.get(pk=task_id)
    task.delete()
    return redirect('todolist')

def edit_task(request, task_id):
    if request.method == "POST":
        task = TaskList.objects.get(pk=task_id)
        form = TaskForm(request.POST or None, instance = task)
        if form.is_valid():
            form.save()
        messages.success(request,("Task edited successfully!"))
        return redirect('todolist')
    else:
        task_obj = TaskList.objects.get(pk=task_id)
        return render(request, 'edit.html', {'task_obj': task_obj})

def complete_task(request, task_id):
    task = TaskList.objects.get(pk=task_id)
    task.done = True
    task.save()
    return redirect('todolist')

def panding_task(request, task_id):
    task = TaskList.objects.get(pk=task_id)
    task.done = False
    task.save()
    return redirect('todolist')
    
def index(request):
    context = {
        'index_text':"Welcome index Page",
    }
    return render(request, 'index.html',context)
