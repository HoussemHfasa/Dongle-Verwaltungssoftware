from django.core.management.base import BaseCommand
from django.utils import timezone
from django.core.mail import send_mail
from Lizenzen.models import Lizenz, UsersKunde
import datetime

class Command(BaseCommand):
    help = "Sends email notifications for licenses that are about to expire."

    def handle(self, *args, **options):
        today = timezone.now().date()
        expiry_date = today + datetime.timedelta(days=3)

        expiring_licenses = Lizenz.objects.filter(ablaufdatum__lte =expiry_date)

        for license in expiring_licenses:
            customer = UsersKunde.objects.get(firmcode=license.dognle_lfd_nr_field.benutzer_firmcode.firmcode)
            subject = "Ihre Lizenz läuft bald ab"
            message = f"Sehr geehrte Kundin, sehr geehrter Kunde,\n\nIhre Lizenz für {license.lizenzname} läuft in 3 Tagen ab. Bitte verlängern Sie Ihre Lizenz, um weiterhin Zugriff auf das Produkt zu haben.\n\nMit freundlichen Grüßen,\nIhr Team"
            from_email = "noreply@example.com"
            to_email = [customer.email]

            send_mail(subject, message, from_email, to_email)

        self.stdout.write(self.style.SUCCESS("E-Mail-Benachrichtigungen gesendet."))