from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from account.models import User

# Create your views here.
@login_required(login_url='signup')
def home(request):
    return render(request,'index.html')


def project(request):
    return render(request,'project.html')


def add_employee(request):
    users = User.objects.filter(role = 'employee', company=request.user.company)
    print(users)
    return render(request,'add-employee.html', {'users': users})


def task_view(request):
    return render(request,'my-task.html')