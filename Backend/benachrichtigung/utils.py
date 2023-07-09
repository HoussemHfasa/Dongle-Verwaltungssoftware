from datetime import datetime, timedelta
from django.core.mail import send_mail
from django.http import HttpResponse
from .models import Lizenz, UserLogginCustomuser

# Funktion zur Überprüfung des Ablaufs von Lizenzen und zum Versenden von E-Mails
def check_lizenzen_ablauf(request):
    today = datetime.now().date()
    expire_in_3_days = today + timedelta(days=3)
    lizenzen = Lizenz.objects.filter(ablaufdatum=expire_in_3_days)

    for lizenz in lizenzen:
        dongle = lizenz.dongle_lfd_nr_field
        kunde = UserLogginCustomuser.objects.filter(firm_code=dongle.benutzer_firmcode)

        if kunde.exists():
            kunde = kunde.first()
            send_mail(
                'Lizenzablauf in 3 Tagen',
                f'Sehr geehrter Kunde, Ihre Lizenz fürdas Produkt {lizenz.lizenzname} läuft in 3 Tagen ab. Bitte erneuern Sie die Lizenz, um weiterhin Zugriff auf das Produkt zu haben.',
                'noreply@example.com',
                [kunde.email],
                fail_silently=False,
            )

    return HttpResponse("E-Mail-Benachrichtigungen wurden gesendet.")