from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from .models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required


from django.conf import settings
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site

# Create your views here.

def signup_view(request):
    
    error_messages = None
    
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        company_name = request.POST.get('company_name')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        
        if User.objects.filter(email=email).exists():
            error_messages = "Email already exists"
            return render(request, 'signup.html', {'error_messages': error_messages})
        
        if password == password2:
            user = User.objects.create_user(
                first_name=first_name,
                last_name=last_name,
                email=email,
                company=company_name,
                password=password,
                username=email,
            )
            
            user.save()
            
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Owner account created successfully!')
                return redirect('home')
            else:
                error_messages = "No User Found !"
        else:
            error_messages = "Passwords doesn't match"
    return render(request, 'signup.html', {'error_messages': error_messages})


def login_view(request):
    error_messages = None
    
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        user = authenticate(request, username=email, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, 'Logged in successfully')
            return redirect('home')
        else:
            error_messages = "Email or password incorrect"
            
    return render(request, 'login.html', {'error_messages': error_messages})

def logout_page(request):
    logout(request)
    messages.success(request, 'Logged out successfully')
    return redirect('login')

@login_required
def create_employee(request):
    
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        employee_position = request.POST.get('employee_position')
        password = request.POST.get('password')
        
        if User.objects.filter(email=email).exists():
            messages.success(request, 'Email already exists')
            return redirect('employee')
        
        user = User.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            email=email,
            position=employee_position,
            role = 'employee',
            password=password,
            username=email,
            company=request.user.company,
        )
        
        
        user.save()
        messages.success(request, 'Employee created successfully!')
        
        # Send email notification
        subject = 'Welcome to the Company'
        current_site = get_current_site(request)
        
        message = render_to_string('employee-mail.html', {
            'first_name': first_name,
            'last_name': last_name,
            'email': email,
            'company': request.user.company,
            'password': password,
        })
        
        from_email = settings.EMAIL_HOST_USER
        to_email = [email,]
        
         # Send the email
        sent_email = EmailMessage(subject, message, from_email, to_email)
        sent_email.content_subtype = 'html'
        sent_email.send()
        
        return redirect('employee')
    
    return render('add-employee.html')


def update_employee(request, id):
    update_employee = User.objects.get(id=id)
    
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        employee_position = request.POST.get('employee_position')
        
        update_employee.first_name=first_name
        update_employee.last_name=last_name
        update_employee.email=email
        update_employee.position=employee_position
        
        update_employee.save()
        messages.success(request, 'Employee Update successfully!')
    
    return redirect('employee')

def delete_employee(request, id):
    remove_employee = User.objects.get(id=id)
    remove_employee.delete()
    
    return redirect('employee')


@login_required
def profile_view(request):
    
    user = User.objects.get(username=request.user.username)
    
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        image = request.FILES.get('image')
        
        if User.objects.filter(email=email).exclude(username=request.user.username).exists():
            messages.error(request, 'Email already exists. Please use a different E-mail address.')
            return redirect('profile')
        
        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        
        if image:
            user.image = image
            
        user.save()
        
        messages.success(request, 'Profile updated successfully!')
        
        return redirect('profile')
            
    return render(request, 'my-account.html', {'user': user})