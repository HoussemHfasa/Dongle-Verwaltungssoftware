# README: MySQL Workbench Installation und Konfiguration mit Django

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
2. Klicken Sie im Menü auf "File" > "Open SQL Script" und wählen Sie das bereitgestellte Initialisierungsskript (z.B. `initialisierungsscript.sql`).
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