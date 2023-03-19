from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from budget.models import Budget
from budget.forms import BudgetForm
from django.contrib.auth.models import User
# Create your views here.

@login_required(login_url='login')
def budgetview(request):
    if (request.method == "GET" and "delete" in request.GET):
        id = request.GET["delete"]
        Budget.objects.filter(id=id).delete()
        return redirect("budget")
    else:
        table_data = Budget.objects.filter(user=request.user)
        context = {
            "table_data": table_data
        }
        return render(request, 'budget/budget.html', context)

@login_required(login_url='login')
def budgetAdd(request):
    if (request.method == "POST"):
        if ("add" in request.POST):
            add_form = BudgetForm(request.POST)
            if (add_form.is_valid()):
                description = add_form.cleaned_data["description"]
                entry = add_form.cleaned_data["category"]
                user = User.objects.get(id=request.user.id)
                actual = add_form.cleaned_data["actual"]
                projected = add_form.cleaned_data["projected"]
                Budget(user=user, description=description, category=entry, actual=actual, projected=projected).save()
                return redirect("budget")
            else:
                context = {
                    "form_data": add_form
                }
                return render(request, 'budget/budget.html', context)
        else:
            return redirect("budget")
    else:
        context = {
            "form_data": BudgetForm()
        }
        return render(request, 'budget/add_budget.html', context)


def budgetEdit(request, id):
    if (request.method == "GET"):
        taskEntry = Budget.objects.get(id=id)
        form = BudgetForm(instance=taskEntry)
        context = { "form_data" : form }
        return render(request, 'budget/edit_budget.html', context)
    elif (request.method == "POST"):
        if ("edit" in request.POST):
            form = BudgetForm(request.POST)
            if (form.is_valid()):
                taskEntry = form.save(commit=False)
                taskEntry.user = request.user
                taskEntry.id = id
                taskEntry.save()
                return redirect("budget")
            else:
                context = {
                    "form_data": form
                }
                return render(request, 'budget/edit_budget.html', context)
        else:
            return redirect("budget")
