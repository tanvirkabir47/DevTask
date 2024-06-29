from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from account.models import User
from .models import Project
from django.contrib import messages

# Create your views here.
@login_required(login_url='signup')
def home(request):
    return render(request,'index.html')


@login_required
def project(request):
    user_company = request.user.company
    projects = Project.objects.filter(user__company=user_company)
    employees = User.objects.filter(role='employee', company=user_company)
    
    return render(request, 'project.html', {'projects': projects, 'employees': employees})

@login_required
def create_project(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            title = request.POST.get('title')
            description = request.POST.get('description')
            employee_ids = request.POST.getlist('employee')  # Get the list of employee IDs from the form
            
            if employee_ids:
                employees = User.objects.filter(id__in=employee_ids, role='employee', company=request.user.company)
            else:
                employees = []

            project = Project(
                user=request.user,
                name=title, 
                description=description,
            )
            project.save() 
            project.employee.set(employees)
            messages.success(request, 'Project created successfully!')
            
            return redirect('project')
        
    
    return render(request, 'project.html')


def add_employee(request):
    users = User.objects.filter(role = 'employee', company=request.user.company)
    
    return render(request,'add-employee.html', {'users': users})


def task_view(request):
    return render(request,'my-task.html')