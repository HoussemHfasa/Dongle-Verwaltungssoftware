-------------------------
## Django-App erstellen
-------------------------

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




--------------------------------------------------------------------
# README: MySQL Workbench Installation und Konfiguration mit Django
--------------------------------------------------------------------


In diesem README finden Sie Anweisungen zur Installation von MySQL Workbench, zur Einrichtung der Datenbank anhand des Initialisierungsskripts und zur Verbindung der Datenbank mit Django in Visual Studio Code.

Schritt 1: MySQL Workbench installieren

1. Gehen Sie zur offiziellen [MySQL Workbench Download-Seite](https://dev.mysql.com/downloads/workbench/).
2. Wählen Sie die passende Version für Ihr Betriebssystem (Windows, macOS, Linux) und laden Sie die Installationsdatei herunter.
3. Führen Sie die heruntergeladene Datei aus und folgen Sie den Anweisungen des Installationsassistenten, um MySQL Workbench zu installieren.

Schritt 2: MySQL Workbench einrichten

1. Öffnen Sie MySQL Workbench und klicken Sie auf das Plus-Symbol (+) neben "MySQL Connections" im Startbildschirm.
2. Geben Sie einen Namen für die Verbindung ein (z.B. "DjangoDB").
3. Setzen Sie die folgenden Parameter:
   - Hostname: die IP-Adresse des MySQL-Servers (z.B. `127.0.0.1` für einen lokalen Server)
   - Port: der Port, auf dem der MySQL-Server läuft (normalerweise `3306`)
   - Username: der Benutzername für den MySQL-Server (z.B. `root`)
   - Password: das Passwort für den MySQL-Server
4. Klicken Sie auf "Test Connection", um sicherzustellen, dass die Verbindung erfolgreich ist.
5. Nach erfolgreicher Verbindung klicken Sie auf "OK", um die Einstellungen zu speichern.

Schritt 3: Datenbank mit Initialisierungsskript erstellen

1. Öffnen Sie die Verbindung, die Sie in Schritt 2 erstellt haben, indem Sie auf den Verbindungsnamen klicken.
2. Klicken Sie im Menü auf "File" > "Open SQL Script" und wählen Sie das bereitgestellte Initialisierungsskript ('Webanwendungdatenbank.sql').
3. Klicken Sie auf das Blitz-Symbol, um das Skript auszuführen und die Datenbank zu erstellen.

Schritt 4: Django-Projekt mit der Datenbank verbinden

1. Öffnen Sie Ihr Django-Projekt in Visual Studio Code.
2. Erstellen Sie eine neue Datei namens `.env` im Hauptverzeichnis Ihres Projekts.
3. Fügen Sie die folgenden Zeilen in die `.env`-Datei ein und passen Sie die Werte entsprechend Ihrer MySQL-Verbindung an:

   ````
   DATABASE_ENGINE=mysql
   DATABASE_NAME=IhrDatenbankName
   DATABASE_USER=IhrBenutzername
   DATABASE_PASSWORD=IhrPasswort
   DATABASE_HOST=IhreIPAdresse
   DATABASE_PORT=IhrPort
   ```

4. Installieren Sie die Python-Pakete `python-dotenv` und `mysqlclient`:

   ````
   pip install python-dotenv mysqlclient
   ```

5. Öffnen Sie die Datei `settings.py` in Ihrem Django-Projekt und fügen Sie die folgenden Zeilen am Anfang der Datei hinzu, um die Umgebungsvariablen aus der `.env`-Datei zu laden:

   ````python
   import os
   from dotenv import load_dotenv

   load_dotenv()
   ```

6. Ändern Sie die DATABASES-Konfiguration in `settings.py`:

   ````python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.mysql',
           'NAME': os.environ['DATABASE_NAME'],
           'USER': os.environ['DATABASE_USER'],
           'PASSWORD': os.environ['DATABASE_PASSWORD'],
           'HOST': os.environ['DATABASE_HOST'],
           'PORT': os.environ['DATABASE_PORT'],
       }
   }
   ```

7. Führen Sie die folgenden Befehle aus, um die Django-Tabellen in der Datenbank zu erstellen:

   ````
   python manage.py makemigrations
   python manage.py migrate
   ```

Jetzt ist Ihr Django-Projekt mit der MySQL-Datenbank verbunden, und Sie können mit der Entwicklung fortfahren.








---------------------------
## React-Projekt erstellen
---------------------------


Dieses Repository enthält eine Anleitung zur Erstellung eines React-Projekts, das in einem Browser geöffnet werden kann.

# Voraussetzungen

Node.js

# Installation

1. Lade das Repository herunter oder klone es mit Git.

2. Stelle sicher, dass Node.js auf deinem Computer installiert ist.

# Schritte
1. Öffne die Kommandozeile oder das Terminal auf deinem Computer.

2. Navigiere zu dem Ordner, in dem du das React-Projekt erstellen möchtest.

3. Erstelle ein neues React-Projekt, indem du den Befehl npx create-react-app my-app in der Kommandozeile ausführst. Ersetze "my-app" durch den Namen deines Projekts.

4. Navigiere in das Projektverzeichnis, indem du cd my-app in der Kommandozeile ausführst.

5. Starte den lokalen Entwicklungsserver, indem du den Befehl npm start in der Kommandozeile ausführst.

6. Öffne einen Webbrowser und navigiere zur URL http://localhost:3000/. Dort solltest du deine React-App sehen.

7. Öffne die Datei src/App.js in einem Texteditor und ändere den Inhalt, um deine App anzupassen.

8. Speichere die Änderungen an der Datei src/App.js.

9. Sieh dir das Ergebnis im Browser an. Jede Änderung, die du an der Datei src/App.js vornimmst, wird automatisch im Browser aktualisiert.




------------------------------
# Django-Projekt mit Anaconda
------------------------------

Dieses Django-Projekt wurde mit Anaconda erstellt und enthält eine -Datei, die alle erforderlichen Pakete und Bibliotheken für das Projekt enthält.requirements.txt


# Installation von Anaconda

1. Laden Sie die Installationsdatei von der Anaconda-Website herunter, die für Ihr Betriebssystem geeignet ist.
2. Öffnen Sie die Installationsdatei und folgen Sie den Anweisungen auf dem Bildschirm, um Anaconda auf Ihrem System zu installieren.

# Verwendung von Anaconda

1. Öffnen Sie das Anaconda-Navigator-Programm, um auf die verschiedenen Pakete und Bibliotheken zuzugreifen, die in Anaconda enthalten sind.
2. Erstellen Sie neue Umgebungen, um verschiedene Projekte zu verwalten und zu isolieren.

# Installation des Projekts
1. Öffnen Sie eine Kommandozeile und navigieren Sie zu dem Verzeichnis, indem das Django-Projekt gespeichert ist.

2. Erstellen Sie eine neue Umgebung in Anaconda mit dem Befehl: 
     conda create -n myenv python=3.8
3.Aktivieren Sie die neue Umgebung mit dem Befehl:
     conda activate myenv
4.Installieren Sie alle erforderlichen Pakete und Bibliotheken aus der -Datei mit dem Befehl:requirements.txt:
     pip install -r requirements.txt

# Verwendung des Projekts
1. Aktivieren Sie die Umgebung, die Sie zuvor erstellt haben, indem Sie den Befehl ausführen:
     conda activate myenv

2.Starten Sie den Django-Entwicklungsserver mit dem Befehl:
     python manage.py runserver
3.Öffnen Sie einen Webbrowser und navigieren Sie zur Adresse, die vom Entwicklungsserver angezeigt wird
4.Sie können nun das Django-Projekt in Ihrem Browser anzeigen und verwenden.