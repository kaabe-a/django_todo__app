from django.shortcuts import render,get_object_or_404,redirect
from . models import Todo
from . forms import TodoForm
from django.urls import reverse
from django.contrib import messages
from django.db.models import Q

# def search_todo(request):
   
#     print(q)
#     if q:
#         todos = Todo.objects.filter(
#         Q(title__contains=q) | Q(description__contains=q)
#         )
#         print(todos)
#     else:
#         todos = Todo.objects.all()
#     context = {
#         'todos':todos
#     }
#     return render(request,'todo/todo.html',context)


def todo_list_view(request):
    query = request.GET.get('search')
    if query:
        todos = Todo.objects.filter(
        Q(title__contains=query) | Q(description__contains=query)
        )
        print(todos)
    else:
        todos = Todo.objects.all()
    context = {
        'todos':todos
    }
    return render(request,'todo/todo.html',context)

def todo_create_view(request):
    if request.method == 'POST':
        form  = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request,'you have created successfully')
    else:
        form = TodoForm()
    context = {
        'form':form
    }
    return render(request,'todo/todo_create.html',context)

def todo_detail_view(request,slug):
    todo = get_object_or_404(Todo,slug=slug)
    context ={
        'todo':todo
    }
    return render(request,'todo/todo_detail.html',context)

def todo_update_view(request,slug):
    todo = get_object_or_404(Todo,slug=slug)
    if request.method == 'POST':
        form = TodoForm(request.POST,instance=todo)
        if form.is_valid():
            form.save()
            messages.info(request,'you have updated successfully')
    else:
        form = TodoForm(instance=todo)
    context = {
        'form':form
    }
    return render(request,'todo/todo_create.html',context)

def todo_delete_view(request,slug):
    todo = get_object_or_404(Todo,slug=slug)
    if request.method == 'POST':
        todo.delete()
        messages.info(request,'you have deleted successfully')
        # return redirect('todo:todo_list') 
        return redirect(reverse('todo:todo_list'))
    context= {
        'todo':todo
    }
    return render(request,'todo/delete_confirm.html',context)
