from django.urls import path , include
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet, dashboard_home

router = DefaultRouter()
router.register(r'tasks' , TaskViewSet , basename = 'task')

urlpatterns = [
    path('', dashboard_home, name='dashboard-home'),
    path('api/' , include(router.urls)),
    path('' , include(router.urls)),
]
