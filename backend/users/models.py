from django.contrib.auth.base_user import BaseUserManager
from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import PermissionsMixin


# Create custom user manager
class CustomUserManager(BaseUserManager):

    def _create_user(self, email, password=None):
        if not email:
            raise ValueError("User must have an email address")
        email = self.normalize_email(email)

        user = self.model(email=email)
        user.set_password(password)
        user.save(using=self.db)

        return user

    def create_user(self, email, password=None):
        user = self._create_user(email=email, password=password)
        user.save(using=self.db)

        return user

    def create_superuser(self, email, password=None):
        user = self._create_user(email=email, password=password)

        user.is_admin = True
        user.save(using=self.db)

        return user


# Create custom user
class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_("Email"), max_length=255, unique=True, blank=False, null=False)
    full_name = models.CharField(_("Full Name"), max_length=50, blank=True, null=True)
    bio = models.CharField(_("Bio"), max_length=230, blank=True, null=True)
    age = models.PositiveIntegerField(_("Age"), blank=True, null=True)
    avatar = models.ImageField(upload_to="users/avatar/", blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []