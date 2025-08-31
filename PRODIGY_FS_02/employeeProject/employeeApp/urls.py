from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name="home"),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('create/', views.employee_create_view, name="employee_create"),
    path('list/', views.employee_list_view, name="employee_list"),
    path('update/<int:pk>/', views.employee_update_view, name="employee_update"),
    path('delete/<int:pk>/', views.employee_delete_view, name="employee_delete"),
]
