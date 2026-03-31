from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from .models import Task

def add_task(request):
    if request.method == "POST":
        task_name = request.POST['task']
        Task.objects.create(task=task_name)
    return redirect('home')

# For mark as done button
def mark_as_done(request , pk):
    task = get_object_or_404(Task,pk =pk)
    task.Is_completed = True
    task.save()

    return redirect('home')

# For undo button (make a button for undone )
def undo(request, pk):
    task = get_object_or_404(Task,pk = pk)
    task.Is_completed = False
    task.save()

    return redirect('home')

# For edit task 
def edit(request , pk):
    get_task = get_object_or_404(Task ,pk = pk)
    if request.method == "POST":
        new_task = request.POST['task']
        get_task.task = new_task
        get_task.save()
        return redirect ('home')
    else :
        context = {
            'get_task': get_task ,
        }

        return render(request , 'edit.html' , context)
    
# Delete Task   
def delete(request,pk):
    delet_task = get_object_or_404(Task ,pk =pk)
    delet_task.delete()

    return redirect('home')
