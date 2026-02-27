from django.http import HttpResponse
from django.shortcuts import render
from todo_app.models import Task 


def home (request):
    task = Task.objects.filter(Is_completed = False).order_by('-updated_at')

    complited_task = Task.objects.filter(Is_completed = True).order_by('-updated_at')

    context = {
        'tasks': task ,
        'complited_task' : complited_task ,

    }


    return render(request ,'home.html',context)