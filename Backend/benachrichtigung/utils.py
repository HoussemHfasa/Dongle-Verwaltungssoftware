from .models import Lizenz, Dongle, UserLogginCustomuser
from datetime import datetime, timedelta
from django.core.mail import send_mail
from django.http import HttpResponse


def check_lizenzen_ablauf(request):
    # Lesen Sie alle Lizenzen aus der Datenbank, deren Ablaufdatumin drei Tagen abläuft.
    today = datetime.now().date()
    expire_in_3_days = today + timedelta(days=3)
    lizenzen = Lizenz.objects.filter(ablaufdatum=expire_in_3_days)

    for lizenz in lizenzen:
        # Lesen Sie das zugehörige `Dongle`-Objekt aus.
        dongle = lizenz.dongle_lfd_nr_field

        # Lesen Sie den zugehörigen Kunden, der die Rolle "Kunde" hat, aus der UserLogginCustomuser-Tabelle aus.
        kunde = UserLogginCustomuser.objects.filter(firm_code=dongle.benutzer_firmcode, role='Kunde').first()

        if kunde is not None:
            # Senden Sie eine E-Mail an den Kunden, um ihn darüber zu informieren, dass seine Lizenz bald abläuft.
            subject = 'Ihre Lizenz läuft bald ab'
            message = f'Ihre Lizenz mit der lfd_Nr {lizenz.lfd_nr_field} läuft in drei Tagen ab. Bitte verlängern Sie Ihre Lizenz, um sicherzustellen, dass Sie weiterhin auf alle Funktionen zugreifen können.'
            from_email = 'djangoverwaltung@gmail.com'
            recipient_list = [kunde.email]
            send_mail(subject, message, from_email, recipient_list)

    return HttpResponse("Lizenzen check completed.")
