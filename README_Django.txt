## Django-App erstellen

Dieses Repository enthält eine Anleitung zur Erstellung eines Django-Projekts, das in einem Browser geöffnet werden kann.

# Anforderungen

Python 311
Django

# Installation

1. Lade das Repository herunter oder klone es mit Git.

2. Stelle sicher, dass Python auf deinem Computer installiert ist.

3. Installiere Django, indem du pip install django in der Kommandozeile ausführst.

# Schritte

1. Erstelle ein neues Django-Projekt, indem du den Befehl django-admin startproject project_name in der Kommandozeile ausführst. Ersetze "project_name" durch den Namen deines Projekts.

2. Navigiere in das Projektverzeichnis, indem du cd project_name ausführst.

3. Erstelle eine neue Django-App, indem du den Befehl python manage.py startapp app_name in der Kommandozeile ausführst. Ersetze "app_name" durch den Namen deiner App.

4.Öffne die Datei settings.py in deinem Django-Projekt. Suche nach der Zeile ALLOWED_HOSTS und füge deine IP-Adresse der Liste der zugelassenen Hosts hinzu, indem du sie als Zeichenkette in der Liste einfügst.
Bsp.: ALLOWED_HOSTS = ['localhost', '127.0.0.1', '192.168.0.100']
```
Ersetze "192.168.0.100" durch deine eigene IP-Adresse.

5. Starte die lokale Entwicklungsserver, indem du python manage.py runserver in der Kommandozeile ausführst.

6. Öffne einen Webbrowser und navigiere zur URL http://localhost:8000/. Dort solltest du deine App sehen und testen können.