from django.shortcuts import render
from rest_framework import viewsets
from .models import Task
from .serializers import TaskSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

# ADD THIS NEW FUNCTION:
def dashboard_home(request):
    return render(request, 'tasks/index.html')
class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    filterset_fields = ['completed' , 'priority']
    search_fields = ['title' , 'description']
    ordering_fields = ['due_date' , 'created_at']

    def get_queryset(self):
        return Task.objects.filter(owner=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
        