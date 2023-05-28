from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from User_loggin.models import CustomUser

User = get_user_model()

class Command(BaseCommand):
    help = 'Create sample data'

    def handle(self, *args, **options):
        # Create admin user
        if not User.objects.filter(email='admin@example.com').exists():
            admin_user = User.objects.create_user(
                email='admin@example.com',
                password='testpassword',
                name='Admin User',
                role='Admin',
            )
            self.stdout.write(self.style.SUCCESS(f'Successfully created admin user: {admin_user.email}'))

        # Create new user
        if not User.objects.filter(email='newuser@example.com').exists():
            new_user = User.objects.create_user(
                email='newuser@example.com',
                name='New User',
                role='Verwalter',
                password='testpassword',
            )
            self.stdout.write(self.style.SUCCESS(f'Successfully created new user: {new_user.email}'))

        # Create kunde user with firm code
        if not User.objects.filter(email='kundeuser@example.com').exists():
            kunde_user = User.objects.create_user(
                email='kundeuser@example.com',
                name='Kunde User',
                role='Kunde',
                password='testpassword',
                firm_code='FIRM123',
            )
            self.stdout.write(self.style.SUCCESS(f'Successfully created kunde user: {kunde_user.email}'))