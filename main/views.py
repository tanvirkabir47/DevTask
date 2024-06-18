from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='signup')
def home(request):
    return render(request,'index.html')


def project(request):
    return render(request,'project.html')


def add_employee(request):
    return render(request,'add-employee.html')


def task_view(request):
    return render(request,'my-task.html')