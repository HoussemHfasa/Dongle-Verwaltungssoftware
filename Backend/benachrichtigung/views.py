from django.shortcuts import render
from DongleAnfordern.models import Ticket
from django.http import JsonResponse

# Funktion, um eine Liste aller Tickets als JSON-Antwort zurückzugeben
def ticket_list(request):
    if request.method == 'GET':
        tickets = Ticket.objects.all()
        ticket_list = list(tickets.values())
        return JsonResponse(ticket_list, safe=False)

# Funktion, um eine Liste der Tickets basierend auf dem firmcode als JSON-Antwort zurückzugeben
def tickets_by_firmcode(request, firmcode):
    if request.method == 'GET':
        tickets = Ticket.objects.filter(kunde=firmcode)
        ticket_list = list(tickets.values())
        return JsonResponse(ticket_list, safe=False)