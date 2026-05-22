from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from django.http import JsonResponse
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Task
from .serializers import TaskSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter


class CustomUserCreationForm(UserCreationForm):
    """Custom form for user registration with better UX."""
    class Meta(UserCreationForm.Meta):
        fields = ('username', 'password1', 'password2')


# Authentication Views
@require_http_methods(["GET", "POST"])
def register(request):
    """Handle user registration."""
    if request.user.is_authenticated:
        return redirect('dashboard')
    
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = CustomUserCreationForm()
    
    return render(request, 'auth/register.html', {'form': form})


@require_http_methods(["GET", "POST"])
def login_view(request):
    """Handle user login."""
    if request.user.is_authenticated:
        return redirect('dashboard')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            return render(request, 'auth/login.html', {'error': 'Invalid credentials'})
    
    return render(request, 'auth/login.html')


@require_http_methods(["POST"])
@login_required(login_url='login')
def logout_view(request):
    """Handle user logout."""
    logout(request)
    return redirect('login')


# Dashboard Views
@login_required(login_url='login')
def dashboard(request):
    """Display main task dashboard."""
    return render(request, 'tasks/dashboard.html')


# API ViewSets
class TaskViewSet(viewsets.ModelViewSet):
    """API endpoint for managing tasks."""
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]
    filterset_fields = ['completed', 'priority']
    search_fields = ['title', 'description']
    ordering_fields = ['due_date', 'created_at']

    def get_queryset(self):
        return Task.objects.filter(owner=self.request.user).order_by('-created_at')
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
        