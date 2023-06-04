#permissions.py
# Permissions importieren 
from rest_framework import permissions

# Eigene Permission-Klasse 
class IsAdminOrReadOnly(permissions.BasePermission):
    # Benutzer muss entweder Admin sein oder nur Lesezugriff 
    def has_permission(self, request, view):
        # Bei sicheren Methoden (GET, HEAD, OPTION) hat jeder Zugriff
        if request.method in permissions.SAFE_METHODS:
            return True 
        # Ansonsten nur Admin-Nutzer 
        return request.user.role == "Admin"