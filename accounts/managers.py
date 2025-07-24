from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self, username, name, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The email field is required.')
        if not username:
            raise ValueError('The username field is required.')
        if not name:
            raise ValueError('The name field is required.')
        email = self.normalize_email(email)
        user = self.model(username=username, name=name, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username=None, name=None, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)
        username = username or extra_fields.get('username')
        name = name or extra_fields.get('name')
        email = email or extra_fields.get('email')
        return self.create_user(username, name, email, password, **extra_fields)

    def create(self, **kwargs):
        if 'password' in kwargs:
            kwargs['password'] = make_password(kwargs.get('password'))
        return super().create(**kwargs)
