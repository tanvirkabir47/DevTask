from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from account.models import User
from .models import Project, Task
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

def single_project(request, slug):
    project = get_object_or_404(Project, slug=slug)
    employees = project.employee.all()
    
    tasks = Task.objects.filter(project=project)
    
    return render(request,'single-project.html', {'project': project, 'employees': employees, 'tasks': tasks})


def add_employee(request):
    users = User.objects.filter(role = 'employee', company=request.user.company)
    
    return render(request,'add-employee.html', {'users': users})


@login_required
def create_task(request, slug):
    project = get_object_or_404(Project, slug=slug)
    
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        due_date = request.POST.get('due_date')
        employee_ids = request.POST.getlist('employee')
        
        # Ensure project is assigned to the task
        task = Task(
            name=name,
            description=description,
            due_date=due_date,
            user=request.user,
            project=project,
        )
        task.save()
        
        # Add employees to the task
        for emp_id in employee_ids:
            employee = User.objects.get(pk=emp_id)
            task.employee.add(employee)
        
        messages.success(request, 'Task created successfully!')
        
        # Redirect to the project page with slug
        return redirect(reverse('single-project', kwargs={'slug': slug}))

    return render(request, 'single-project.html', {'project': project})

def task_view(request):
    return render(request,'my-task.html')


