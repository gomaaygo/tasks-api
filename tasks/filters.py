# filters.py
import django_filters

from .models import Task, Category

class TaskFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    description = django_filters.CharFilter(lookup_expr='icontains')
    status = django_filters.CharFilter()
    execute_at = django_filters.DateFilter()
    categories = django_filters.ModelMultipleChoiceFilter(queryset=Category.objects.all())

    class Meta:
        model = Task
        fields = ['title', 'description', 'status', 'execute_at', 'categories']
