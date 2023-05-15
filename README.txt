## Django-App erstellen
Dieses Repository enthält eine grundlegende Anleitung zur Erstellung einer Django-App.

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

4. Definiere die Attribute deiner Modelle und ihre Beziehungen zueinander in der models.py-Datei in deinem App-Verzeichnis.

5. Führe Migrationen aus, indem du python manage.py makemigrations und python manage.py migrate in der Kommandozeile ausführst.

6. Definiere die Logik, die deine App ausführt, wenn eine bestimmte URL aufgerufen wird, in der views.py-Datei in deinem App-Verzeichnis.

7. Definiere, welche Views aufgerufen werden, wenn eine bestimmte URL aufgerufen wird, in der urls.py-Datei in deinem App-Verzeichnis.

8. Erstelle HTML-Templates, die definieren, wie die Daten, die du aus der Datenbank abrufst, in HTML-Code umgewandelt werden, indem du den templates-Ordner in deinem App-Verzeichnis erstellst und HTML-Dateien darin ablegst.

9. Starte die lokale Entwicklungsserver, indem du python manage.py runserver in der Kommandozeile ausführst.

10. Öffne einen Webbrowser und navigiere zur URL http://localhost:8000/. Dort solltest du deine App sehen und testen können.