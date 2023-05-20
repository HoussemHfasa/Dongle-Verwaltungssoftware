from django.shortcuts import render
from django.http import JsonResponse

def create_ticket(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        dongle_id = request.POST.get('dongleId')
        handler = request.POST.get('handler')
        customer_name = request.POST.get('kundenName')
        expiration_date = request.POST.get('ablaufdatum')

        # Speichern Sie die Daten in der Datenbank oder führenandere notwendige Schritte aus

        # Rückgabe einer JSON-Antwort mit den erstellten Ticket-Daten
        return JsonResponse({'title': title, 'dongle_id': dongle_id, 'handler': handler, 'customer_name': customer_name, 'expiration_date': expiration_date})
    else:
        # Rückgabe einer Fehlerantwort, wenn die Anfrage nicht POST ist
        return JsonResponse({'error': 'Invalid request method'})