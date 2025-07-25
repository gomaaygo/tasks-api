from django.db import models

from common.models import TimeStampedModel


class Category(TimeStampedModel):
    name = models.CharField(max_length=100, unique=True, blank=False, db_index=True, null=False, verbose_name='Nome')
    icon = models.CharField(max_length=100, blank=True, null=True, verbose_name='Ícone')

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['name']

    def __str__(self):
        return self.name


class Task(TimeStampedModel):
    user = models.ForeignKey('accounts.User', on_delete=models.CASCADE, db_index=True, related_name='tasks', verbose_name='Usuário')
    title = models.CharField(max_length=200, blank=False, null=False, verbose_name='Título')
    description = models.TextField(blank=True, null=True, verbose_name='Descrição')
    categories = models.ManyToManyField(Category, related_name='tasks', blank=True, verbose_name='Categorias')
    status = models.CharField(
        max_length=50,
        choices=(
            ('pending', 'Pendente'),
            ('in_progress', 'Em andamento'),
            ('completed', 'Concluída'),
        ),
        db_index=True,
        default='in_progress',
    )
    execute_at = models.DateTimeField(db_index=True, verbose_name='Data de execução')

    class Meta:
        verbose_name = 'Tarefa'
        verbose_name_plural = 'Tarefas'
        ordering = ['-created_at']

    def __str__(self):
        return self.title

