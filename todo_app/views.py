from django.shortcuts import render, redirect
from .models import Task

def add_task(request):
    if request.method == "POST":
        task_name = request.POST['task']
        Task.objects.create(task=task_name)
    return redirect('home')