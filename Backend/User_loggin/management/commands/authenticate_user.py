from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

User = get_user_model()

class Command(BaseCommand):
    help = "Authenticate a user using email and password"

    def handle(self, *args, **options):
        email = input("Enter your email: ")
        password = input("Enter your password: ")
        role = self.authenticate_user(email, password)
        self.stdout.write(self.style.SUCCESS(role))

    def authenticate_user(self, email, password):
        try:
            user = User.objects.get(email=email)
            if user.check_password(password):
                return user.role
            else:
                return "Invalid password"
        except User.DoesNotExist:
            return "User does not exist"