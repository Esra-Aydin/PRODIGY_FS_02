from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.contrib.auth.models import User
from django.contrib import messages

from .forms import EmployeeForm, RegisterForm
from .models import Employee


# ---------------- AUTH VIEWS ---------------- #

def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = User.objects.create_user(username=username, password=password)
            login(request, user)
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'accounts/register.html', {'form': form})


def login_view(request):
    error_message = ""
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            next_url = request.POST.get('next') or request.GET.get('next') or 'home'
            return redirect(next_url)
        else:
            error_message = "Invalid username or password."
    return render(request, "accounts/login.html", {'error': error_message})


def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect('login')
    else:
        return redirect('home')


@login_required
def home_view(request):
    return render(request, 'employeeApp/home.html')


# ---------------- EMPLOYEE CRUD VIEWS ---------------- #

@login_required
def employee_create_view(request):
    form = EmployeeForm()
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Employee added successfully.")
            return redirect('employee_list')
    return render(request, 'employeeApp/employee_form.html', {'form': form})


@login_required
def employee_list_view(request):
    employees = Employee.objects.all()
    return render(request, 'employeeApp/employee_list.html', {'employees': employees})


@login_required
def employee_update_view(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    form = EmployeeForm(instance=employee)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            messages.success(request, "Employee updated successfully.")
            return redirect('employee_list')
    return render(request, 'employeeApp/employee_form.html', {'form': form})


@login_required
def employee_delete_view(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':
        employee.delete()
        messages.success(request, "Employee deleted successfully.")
        return redirect('employee_list')
    return render(request, 'employeeApp/employee_confirm_delete.html', {'employee': employee})
