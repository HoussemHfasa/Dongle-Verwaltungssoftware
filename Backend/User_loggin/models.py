# Abstrakte Nutzermodelle importieren
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager, 
    PermissionsMixin,
) 

# Models importieren 
from django.db import models

# Übersetzungen importieren 
from django.utils.translation import gettext_lazy as _


# Eigene Manager-Klasse 
class CustomUserManager(BaseUserManager): 
    # Nutzer per natürlicher ID (Email) abrufen
    def get_by_natural_key(self, email):
        return self.get(email=email)

    # Nutzer erstellen 
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("Die E-Mail muss gesetzt sein.") 
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    # Superuser erstellen 
    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser muss is_staff=True haben.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser muss is_superuser=True haben.")

        return self.create_user(email, password, **extra_fields)


# Eigene Nutzermodel 
class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    role = models.CharField(
        # Nutzerrollen zur Auswahl
        max_length=10,  
        choices=[("Admin", "Admin"), ("Verwalter", "Verwalter"), ("Kunde", "Kunde")],
    )
    firm_code = models.CharField(max_length=255, blank=True, null=True) 

    
    # Eigene Berechtigung
    class Meta:
        permissions = [("can_view_user", "Can view user")]
       

    # Eigene Manager-Klasse
    objects = CustomUserManager()

    # Nutzer mit E-Mail authentifizieren 
    USERNAME_FIELD = "email"
    # Benötigte Felder 
    REQUIRED_FIELDS = ["name", "role"]

    # Nutzerrepräsentation 
    def __str__(self):
        return self.email