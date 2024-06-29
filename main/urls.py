from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('project/', views.project, name='project'),
    path('create-project/', views.create_project, name='create-project'),
    path('single-project/<slug:slug>', views.single_project, name='single-project'),
    path('employee/', views.add_employee, name='employee'),
    path('task/', views.task_view, name='task'),
    path('create-task/<slug:slug>', views.create_task, name='create-task'),
]