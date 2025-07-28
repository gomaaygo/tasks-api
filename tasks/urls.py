from django.urls import path

from .views import TaskViewSet

app_name = 'tasks'

urlpatterns = [
    path('', TaskViewSet.as_view({'post': 'create', 'get': 'list'}), name='task-list'),
    path('<int:pk>', TaskViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'update', 'delete': 'destroy'}), name='task-detail'),
]
