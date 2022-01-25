# Add your Views Here
from django.shortcuts import render
from django.http import HttpResponseRedirect
from tasks.models import Task


def tasks_view(request):
    search_term = request.GET.get("search")
    tasks = Task.objects.filter(deleted=False).filter(completed=False)
    if search_term:
        tasks = Task.objects.filter(title__icontains=search_term).filter(deleted=False).filter(completed=False)
    
    return render(request,"tasks.html", {"tasks": tasks}) 

def completed_tasks_view(request):
    completed_tasks = Task.objects.filter(completed=True)
    return render(request,"completed.html", {"tasks": completed_tasks}) 

def add_task_view(request):
    task_val = request.GET.get("task")
    Task(title=task_val).save()
    return HttpResponseRedirect("/tasks") 

def delete_task_view(request, idx):
    Task.objects.filter(id=idx).update(deleted=True)
    return HttpResponseRedirect("/tasks") 

def complete_task_view(request, idx):
    Task.objects.filter(id=idx).update(completed=True)
    return HttpResponseRedirect("/tasks") 

def all_tasks_view(request):
    tasks = Task.objects.filter(deleted=False).filter(completed=False)
    completed_tasks = Task.objects.filter(completed=True)
    return render(request,"all_tasks.html", {"pending": tasks, "completed": completed_tasks}) 