from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from datetime import datetime
from .models import Ticket
from .models import Dongle

@csrf_exempt
def create_ticket(request):
    if request.method == 'POST':
        # Lese die Daten aus dem POST-Request
        data = request.POST
        dongle_id = data.get('dongleId')
        product_name = data.get('productName')
        email = data.get('email')
        handler = data.get('handler')
        ablaufdatum = data.get('ablaufdatum')

        # Finde den Dongle-Eintrag in der Datenbank
        dongle = Dongle.objects.get(Serien_Nr=dongle_id)

        # Erstelle das neue Ticket
        ticket = Ticket(
            Titel=product_name,
            Status='offen',
            Erstellungsdatum=datetime.now(),
            Admin_Verwalter_ID=None,
            Schließungsdatum=None,
            Dongle_Lfd_Nr=dongle.Lfd_Nr,
            Benutzer_Firmcode=dongle.Benutzer_Firmcode        )

        # Speichere das Ticket in der Datenbank
        ticket.save()

        # Gebe eine JSON-Antwort zurück
        response_data = {'message': 'Ticket erfolgreich erstellt!'}
        return JsonResponse(response_data)