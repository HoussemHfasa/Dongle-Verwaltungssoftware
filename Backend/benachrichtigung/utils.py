from datetime import datetime, timedelta
from django.core.mail import send_mail
from .models import Lizenz, Kunde, Dongle
from django.http import HttpResponse



def check_lizenzen_ablauf(request):
    # Lesen Sie alle Lizenzen aus der Datenbank, deren Ablaufdatum in drei Tagen abläuft.
    today = datetime.now().date()
    expire_in_3_days = today + timedelta(days=3)
    lizenzen = Lizenz.objects.filter(ablaufdatum=expire_in_3_days)

    for lizenz in lizenzen:
        # Lesen Sie die zugehörige `Dognle_Lfd. Nr.` aus und suchen Sie nach einer entsprechenden `Lfd. Nr.` in der Dongle-Tabelle.
        dongle_lfd_nr = lizenz.dognle_lfd_nr_field
        dongle = Dongle.objects.filter(lfd_nr=dongle_lfd_nr).first()

        if dongle is not None:
            kunde = Kunde.objects.filter(firmcode=dongle.benutzer_firmcode).first()

            if kunde is not None:
                def send_email_notification():
                    # Senden Sie eine E-Mail an den Kunden, um ihn darüber zu informieren, dass seine Lizenz bald abläuft.
                    subject = 'Ihre Lizenz läuft bald ab'
                    message = f'Ihre Lizenz mit der Seriennummer {lizenz.seriennummer} läuft in drei Tagen ab. Bitte verlängern Sie Ihre Lizenz, um sicherzustellen, dass Sie weiterhin auf alle Funktionen zugreifen können.'
                    from_email = 'admin@example.com'
                    recipient_list = [kunde.email]
                    send_mail(subject, message, from_email, recipient_list)
                    
          
