from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from .managers import UserManager
from common.models import TimeStampedModel


class User(AbstractBaseUser, PermissionsMixin, TimeStampedModel):
    name = models.CharField(max_length=150, verbose_name='Nome')
    username = models.CharField(max_length=150, unique=True, db_index=True, verbose_name='Username')
    email = models.EmailField(max_length=255, unique=True, db_index=True, error_messages={'unique': 'User with existing email.'}
                              , verbose_name='Email')
    is_active = models.BooleanField(default=True,
        help_text=('Designates whether this user should be treated as active. Unselect this instead of deleting accounts.'),
        verbose_name='Ativo?')
    is_staff = models.BooleanField(default=False,
        help_text=('Designates whether the user can log into this admin site.'),
        verbose_name='Acesso ao Dashboard?')

    objects = UserManager()

    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'
        ordering = ['-created_at']

    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.email
