from django.db import models

from common.models import TimeStampedModel


class Category(TimeStampedModel):
    name = models.CharField(max_length=100, unique=True, blank=False, db_index=True, null=False, verbose_name='Category Name')
    icon = models.CharField(max_length=100, blank=True, null=True, verbose_name='Icon')

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['name']

    def __str__(self):
        return self.name


