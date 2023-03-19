from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import  render, redirect
from django.contrib.auth.decorators import login_required
from core.forms import JoinForm, LoginForm
from tasks.models import Task
from budget.models import Budget
# Create your views here.

@login_required(login_url='login')
def coreview(request):
    if(request.method == "GET"):
        task_data = Task.objects.filter(user=request.user)
        budget_data = Budget.objects.filter(user=request.user)
        context = {
            "task_data": task_data,
            "budget_data": budget_data
        }
        return render(request, 'core/core.html', context)

def join_action(request):
    if (request.method == "POST"):
        join_form = JoinForm(request.POST)
        if (join_form.is_valid()):
            user = join_form.save()
            user.set_password(user.password)
            user.save()
            return redirect("login")
        else:
            context = {"join_form": join_form}
            return render(request, 'join.html', context)
    else:
        join_form = JoinForm()
        page_data = {"join_form": join_form}
        return render(request, 'join.html', page_data)


def login_action(request):
    if (request.method == 'POST'):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data["username"]
            password = login_form.cleaned_data["password"]
            user = authenticate(username=username, password=password)
            if user:
                if user.is_active:
                    login(request, user)
                    return redirect("/")
                else:
                    return HttpResponse("Your account is not active.")
            else:
                print("Someone tried to login and failed.")
                print("They used username: {} and password: {}".format(
                    username, password))
                return render(request, 'login.html', {"login_form": LoginForm})
    else:
        return render(request, 'login.html', {"login_form": LoginForm})


def user_logout(request):
    logout(request)
    return redirect('login')


def about(request):
    return render(request, 'about.html')