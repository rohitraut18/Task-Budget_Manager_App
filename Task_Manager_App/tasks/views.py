from django.shortcuts import render, redirect
from tasks.models import Task
from django.contrib.auth.decorators import login_required
from tasks.forms import TaskForm
from django.contrib.auth.models import User
# Create your views here.

@login_required(login_url='login')
def taskview(request):
    if (request.method == "GET" and "delete" in request.GET):
        id = request.GET["delete"]
        Task.objects.filter(id=id).delete()
        return redirect("tasks")
    else:
        table_data = Task.objects.filter(user=request.user)
        context = {
            "table_data": table_data
        }
        return render(request, 'tasks/tasks.html', context)

@login_required(login_url='login')
def add(request):
    if (request.method == "POST"):
        if ("add" in request.POST):
            add_form = TaskForm(request.POST)
            if (add_form.is_valid()):
                description = add_form.cleaned_data["description"]
                entry = add_form.cleaned_data["category"]
                user = User.objects.get(id=request.user.id)
                Task(user=user, description=description,
                             category=entry).save()
                return redirect("tasks")
            else:
                context = {
                    "form_data": add_form
                }
                return render(request, 'tasks/add_task.html', context)
        else:
            return redirect("tasks")
    else:
        context = {
            "form_data": TaskForm()
        }
        return render(request, 'tasks/add_task.html', context)


@login_required(login_url='login')
def edit(request, id):
	if (request.method == "GET"):
		taskEntry = Task.objects.get(id=id)
		form = TaskForm(instance=taskEntry)
		context = { "form_data" : form }
		return render(request, 'tasks/edit_task.html', context)
	elif (request.method == "POST"):
		if ("edit" in request.POST):
			form = TaskForm(request.POST)
			if (form.is_valid()):
				taskEntry = form.save(commit=False)
				taskEntry.user = request.user
				taskEntry.id = id
				taskEntry.save()
				return redirect("tasks")
			else:
				context = {
				"form_data": form
				}
				return render(request, 'tasks/add_task.html', context)
		else:
			return redirect("tasks")


@login_required(login_url='login')
def complete(request, id):
    task = Task.objects.filter(id=id)[0]
    if task.completed:
        task.completed = False
    else:
        task.completed = True
    task.save()
    return redirect('tasks')
