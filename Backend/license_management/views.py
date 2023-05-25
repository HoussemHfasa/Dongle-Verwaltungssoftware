from datetime import datetime, timedelta
from django.core.mail import send_mail
from django.http import HttpResponse
from license_management.models import Lizenz, Kunde


def check_license_expiry():
    today = datetime.now().date()
    expiry_date = today + timedelta(days=3)
    licenses = Lizenz.objects.filter(ablaufdatum__lte=expiry_date)
    users = []
    for license in licenses:
        user = Kunde.objects.get(firmcode=license.dognle_lfd_nr_field.benutzer_firmcode)
        if user.e_mail:
            users.append({'name': user.name, 'email': user.e_mail})
    return users


def send_expiry_notification(user):
    subject = 'Ihre Lizenz läuft bald ab'
    message = f'Hallo {user["name"]}, Ihre Lizenz läuft in drei Tagen ab. Bitte verlängern Sie Ihre Lizenz, ' \
              f'um weiterhin das Produkt nutzen zu können.'
    from_email = 'noreply@example.com'
    recipient_list = [user['email']]
    send_mail(subject, message, from_email, recipient_list)


def run_expiry_check(request):
    users = check_license_expiry()
    for user in users:
        send_expiry_notification(user)
    return HttpResponse('Die Überprüfung der Lizenzabläufe wurde erfolgreich ausgeführt.')
