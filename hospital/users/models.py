from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class UserManager(BaseUserManager):
    def create_user(self, email, phone, username, password=None,**extra_fields):
        if not email and not phone:
            raise ValueError("Email or phone is required")
        ne=self.normalize_email(email)
        user = self.model(email=ne, phone=phone, username=username ,**extra_fields)
        user.set_password(password)
        user.save()
        return user
    def create_staffuser(self, email, phone, username, password=None):
        user = self.create_user(email, phone, username, password)
        user.is_staff = True
        user.is_active = True
        user.save(using=self._db)
        return user


    def create_superuser(self, email, phone, username, password=None):
        user = self.create_user(email, phone, username, password)
        user.is_staff = True
        user.is_active=True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True, null=True, blank=True)
    phone = models.CharField(max_length=15, unique=True, null=True, blank=True)
    username = models.CharField(max_length=50)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['phone', 'username']

    objects = UserManager()

    def __str__(self):
        return self.email or self.phone

