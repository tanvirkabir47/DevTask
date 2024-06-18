from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('project/', views.project, name='project'),
    path('employee/', views.add_employee, name='employee'),
    path('task/', views.task_view, name='task'),
]