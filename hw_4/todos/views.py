from django.shortcuts import render, get_object_or_404, redirect
from .models import TodoList, Todo
from .forms import TodoListForm, TodoForm

def todo_list(request):
    lists = TodoList.objects.all()
    return render(request, "todos/todo_list.html", {"todo_lists": lists})

def todo_detail(request, id):
    todo_list = get_object_or_404(TodoList, id=id)
    todos = todo_list.todo_set.all()
    return render(request, "todos/todo_detail.html", {"todo_list": todo_list, "todos": todos})

def todo_delete(request, id):
    todo_list = get_object_or_404(TodoList, id=id)
    todo_list.delete()
    return redirect("todo_list")

def todo_edit(request, id):
    todo_list = get_object_or_404(TodoList, id=id)
    if request.method == "POST":
        form = TodoListForm(request.POST, instance=todo_list)
        if form.is_valid():
            form.save()
            return redirect("todo_detail", id=id)
    else:
        form = TodoListForm(instance=todo_list)
    return render(request, "todos/todo_edit.html", {"form": form})

def task_delete(request, id):
    todo = get_object_or_404(Todo, id=id)
    list_id = todo.todo_list.id
    todo.delete()
    return redirect("todo_detail", id=list_id)

def task_edit(request, id):
    todo = get_object_or_404(Todo, id=id)
    if request.method == "POST":
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect("todo_detail", id=todo.todo_list.id)
    else:
        form = TodoForm(instance=todo)
    return render(request, "todos/todo_edit.html", {"form": form})

