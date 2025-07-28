from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Task
from .serializers import TaskCreateSerializer, TaskUpdateSerializer
from accounts.permissions import IsOwnerOrReadOnly


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user).order_by('execute_at')

    def get_serializer_class(self):
        if self.action == 'create':
            return TaskCreateSerializer
        return TaskUpdateSerializer
