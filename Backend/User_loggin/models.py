from django.contrib.auth.models import Group, Permission
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils.translation import gettext_lazy as _

# Create your models here.
class AdminVerwalterManager(BaseUserManager):
    # Implementieren Sie die Methoden zum Erstellen von Benutzern und Superbenutzern
    ...

class KundeManager(BaseUserManager):
    # Implementieren Sie die Methoden zum Erstellen von Benutzern und Superbenutzern
    ...

class AdminVerwalter(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    role = models.CharField(max_length=10, choices=[('Admin', 'Admin'), ('Verwalter', 'Verwalter')])
    groups = models.ManyToManyField(
        Group,
        verbose_name=_('groups'),
        blank=True,
        help_text=_(
            'The groups this user belongs to. A user will get all permissions '
            'granted to each of their groups.'
        ),
        related_name="admin_verwalter_set",
        related_query_name="admin_verwalter",
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=_('user permissions'),
        blank=True,
        help_text=_('Specific permissions for this user.'),
        related_name="admin_verwalter_set",
        related_query_name="admin_verwalter",
    )

    objects = AdminVerwalterManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'role']

    class Meta:
        pass

class Kunde(AbstractBaseUser, PermissionsMixin):
    firmcode = models.CharField(max_length=255, primary_key=True)
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)

    groups = models.ManyToManyField(
        Group,
        verbose_name=_('groups'),
        blank=True,
        help_text=_(
            'The groups this user belongs to. A user will get all permissions '
            'granted to each of their groups.'
        ),
        related_name="kunde_set",
        related_query_name="kunde",
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=_('user permissions'),
        blank=True,
        help_text=_('Specific permissions for this user.'),
        related_name="kunde_set",
        related_query_name="kunde",
    )

    objects = KundeManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'firmcode']

    class Meta:
        pass