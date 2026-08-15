from django.shortcuts import render,get_object_or_404,redirect
from .models import Todo

# Create your views here.

# get all
def todo_list(request):
    todo = Todo.objects.all().order_by('id')
    return render(request, 'home.html', {'todo': todo})

# get one using ID
def view_todo(request, id):
    todo = get_object_or_404(Todo, id =id)

    if request.method== 'POST':
        todo.status = request.POST.get('status') == 'true'
        todo.save()
        return redirect('view_todo', id=todo.id)
    
    return render(request, 'view.html', {'todo':todo})

# Add
def add_todo(request):
    if request.method == 'POST':
        _title = request.POST.get('title')
        _description = request.POST.get('description')
        Todo.objects.create( title = _title, description = _description )
        return redirect('home')

    return render(request, 'add.html')
    
# Edit
def edit_todo(request, id):
    todo = get_object_or_404(Todo, id=id)

    if request.method == 'POST':
        todo.title = request.POST.get('title')
        todo.description = request.POST.get('description')
        todo.status = request.POST.get('status') == 'true'
        todo.save()
        return redirect('view_todo', id=todo.id)

    return render(request, 'edit.html', {'todo': todo})


# Delete
def delete_todo(request, id):
    todo = get_object_or_404(Todo, id=id)

    if request.method == 'POST':
        todo.delete()
        return redirect('home')

    return render(request, 'delete.html', {'todo': todo})

