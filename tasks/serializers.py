from rest_framework import serializers

from tasks.models import Task


class TaskCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = ('title', 'description', 'categories', 'status', 'execute_at')
        read_only_fields = ('id', 'user', 'created_at')
        extra_kwargs = {
            'title': {'required': True, 'allow_blank': False},
            'status': {'required': True, 'allow_null': False},
        }

    def create(self, validated_data):
        user = self.context['request'].user
        validated_data.pop('user', None)
        categories = validated_data.pop('categories', [])
        task = Task.objects.create(user=user, **validated_data)
        task.categories.set(categories)
        return task


class TaskUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('title', 'description', 'categories', 'status', 'execute_at')
        read_only_fields = ('id', 'user', 'created_at')
        extra_kwargs = {
            'title': {'required': False},
            'execute_at': {'required': False},
        }
