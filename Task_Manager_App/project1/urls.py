"""project1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from core import views as core_views
from tasks import views as tasks_views
from budget import views as budget_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', core_views.coreview, name='home'),
    path('login/', core_views.login_action, name='login'),
    path('join/', core_views.join_action, name='join'),
    path('budget/', budget_views.budgetview, name='budget'),
    path('logout/', core_views.user_logout, name='logout'),
    path('about/', core_views.about, name='about'),
    path('tasks/', tasks_views.taskview, name='tasks'),
    path('tasks/add/', tasks_views.add, name = "add"),
    path('tasks/edit/', tasks_views.edit, name = "edit"),
    path('tasks/edit/<int:id>/', tasks_views.edit, name = "editNO"),
    path('tasks/complete', tasks_views.taskview, name="complete"),
    path('tasks/complete/<int:id>', tasks_views.complete, name = "completeNO"),
    path('budget/add/', budget_views.budgetAdd, name="budgetAdd"),
    path('budget/edit/', budget_views.budgetEdit, name="budgetEdit"),
    path('budget/edit/<int:id>/', budget_views.budgetEdit, name="budgetEdit"),
   
]


 
