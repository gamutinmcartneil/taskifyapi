from django.conf import settings
from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
    User
)


class UserRole(models.Model):
    """User Role in the system."""
    name = models.CharField(max_length=255, null=True)
    description = models.TextField(max_length=255)

    def __str__(self):
        return self.name

class UserManager(BaseUserManager):
    """Manager for users."""

    def create_user(self, username, password=None,  **extra_fields):
        """Create, save and return a new user."""
        if not username:
            raise ValueError('User must have an username')
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self.db)

        return user

    def create_superuser(self, username, password):
        """Create and return a new superuser."""

        user = self.create_user(username, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self.db)

        return user
    
class User(AbstractBaseUser, PermissionsMixin ):
    """User in the system."""
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(max_length=255)
    initial = models.CharField(max_length=255, null=True)
    first_name = models.CharField(max_length=255, null=True)
    middle_name = models.CharField(max_length=255, null=True)
    last_name = models.CharField(max_length=255, null=True)
    address = models.CharField(max_length=255, null=True)
    joined = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    role = models.ForeignKey(UserRole, related_name='user_role', on_delete=models.CASCADE, null=True)

    objects = UserManager()

    USERNAME_FIELD = 'username'

    def __str__(self):
        return self.username

class Priority(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=255)
    status = models.CharField(max_length=255)

class Task(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=255)
    priority = models.ForeignKey(Priority,related_name='priority',on_delete=models.CASCADE, null=True)
    assignedto = models.ForeignKey(User, related_name='user', on_delete=models.CASCADE, null=True)
    status = models.CharField(max_length=255, null=True)
    isdeleted = models.BooleanField(null=True)
