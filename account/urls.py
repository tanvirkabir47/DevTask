from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_page, name='logout'),
]