#importing Task and Taskform method from their files
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Task
from .forms import TaskForm


def task_list(request):
    tasks=Task.objects.all()
    return render(request,'tasks/task_list.html',{'tasks':tasks})


def task_create(request):
    if request.method=="POST":
        form=TaskForm(request.POST)
        if form.is_valid():
            task=form.save(commit=False)
            task.user=request.user
            task.save()
            return redirect(task_list)
        
    else:
        form=TaskForm()
    return render(request,"tasks/task_form.html",{"form":form})    


def task_update(request,task_id):
    tasks=Task.objects.get(id=task_id,user=request.user)
    if request.method == "POST":
        form=TaskForm(request.POST,instance=tasks)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form=TaskForm(instance=tasks)
    return render(request,"tasks/task_form.html",{"form":form})


def task_delete(request,task_id):
    tasks=Task.objects.get(id=task_id,user=request.user)
    if request.method == "POST":
        tasks.delete()
        return redirect(task_list)
    return render(request,"tasks/tasks_confirm.html",{'tasks':tasks})
    
