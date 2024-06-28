from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_page, name='logout'),
    path('create-employee/', views.create_employee, name='create-employee'),
    path('update-employee/<int:id>', views.update_employee, name='update-employee'),
    path('delete-employee/<int:id>', views.delete_employee, name='delete-employee'),
]