from django.urls import path
from . import views

urlpatterns = [
    path('', views.signin, name='signin'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('admin_/', views.admin, name='admin_'),
]