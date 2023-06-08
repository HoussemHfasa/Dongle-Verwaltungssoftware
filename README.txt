# Django-Projekt mit Anaconda
------------------------------

Dieses Django-Projekt wurde mit Anaconda erstellt und enthält eine `requirements.txt`-Datei, die alle erforderlichen Pakete und Bibliotheken für das Projekt auflistet.

## Installation von Anaconda

1. Laden Sie die Installationsdatei von der [Anaconda-Website](https://www.anaconda.com/products/distribution) herunter, die für Ihr Betriebssystem geeignet ist.
2. Öffnen Sie die Installationsdatei und folgen Sie den Anweisungen auf dem Bildschirm, um Anaconda auf Ihrem System zu installieren.

## Installation von nvm (Node Version Manager) für Windows

1. Laden Sie die `nvm-setup.exe`-Datei aus dem Ordner `\team01\Node installation` herunter oder besuchen Sie diesen [Link](https://github.com/coreybutler/nvm-windows/releases), um die neueste Version von nvm für Windows herunterzuladen.
2. Führen Sie die heruntergeladene `nvm-setup.exe`-Datei aus und folgen Sie den Anweisungen auf dem Bildschirm, um nvm auf Ihrem System zu installieren.

Nach der Installation von Anaconda und nvm können Sie mit den folgenden Schritten fortfahren.

## Verwendung von Anaconda

### Installation des Projekts

1. Öffnen Sie eine Kommandozeile oder ein Terminal und navigieren Sie zu dem Verzeichnis, in dem das Django-Projekt gespeichert ist. Verwenden Sie dazu den Befehl `cd (Pfad des Backend)`.

2. Erstellen Sie eine neue Umgebung in Anaconda mit dem Befehl: `conda create -n myenv python=3.8`.

3. Aktivieren Sie die neue Umgebung mit dem Befehl: `conda activate myenv`.

4. Installieren Sie Django in dieser Umgebung mit dem Befehl: `conda install django`.

5. Installieren Sie alle erforderlichen Pakete und Bibliotheken aus der `requirements.txt`-Datei mit dem Befehl: `pip install -r requirements.txt`.

### Installation von Node.js

1. Öffnen Sie eine Kommandozeile oder ein Terminal und führen Sie den Befehl `nvm install 16` aus, um Node.js Version 16 zu installieren.

2. Führen Sie den Befehl `nvm use 16` aus, um die installierte Node.js-Version zu verwenden.

### Verwendung des Projekts

1. Aktivieren Sie die Umgebung, die Sie zuvor erstellt haben, indem Sie den Befehl ausführen: `conda activate myenv`.

2. Starten Sie den Django-Entwicklungsserver mit dem Befehl: `python manage.py runserver`.

3. Öffnen Sie einen Webbrowser und navigieren Sie zur Adresse, die vom Entwicklungsserver angezeigt wird.

4. Sie können nun das Django-Projekt in Ihrem Browser anzeigen und verwenden.

## Schritt 2: MySQL Workbench einrichten

1. Öffnen Sie MySQL Workbench und klicken Sie auf das Plus-Symbol (+) neben "MySQL Connections" im Startbildschirm.
2. Geben Sie einen Namen für die Verbindung ein (z.B. "DjangoDB").
3. Setzen Sie die folgenden Parameter:
   - Hostname: die IP-Adresse des MySQL-Servers (z.B. `127.0.0.1` für einen lokalen Server)
   - Port: der Port, auf dem der MySQL-Server läuft (normalerweise `3306`)
   - Username: der Benutzername für den MySQL-Server (z.B. `root`)
   - Password: das Passwort für den MySQL-Server
4. Klicken Sie auf "Test Connection", um sicherzustellen, dass die Verbindung erfolgreich ist.
5. Nach erfolgreicher Verbindung klicken Sie auf "OK", um die Einstellungen zu speichern.

## Schritt 3: Datenbank mit Initialisierungsskript erstellen

1. Öffnen Sie die Verbindung, die Sie in Schritt 2 erstellt haben, indem Sie auf den Verbindungsnamen klicken.
2. Klicken Sie im Menü auf "File" > "Open SQL Script" und wählen Sie das bereitgestellte Initialisierungsskript ('dongle1.sql').
3. Klicken Sie auf das Blitz-Symbol, um das Skript auszuführen und die Datenbank zu erstellen.

## Schritt 4: Django-Projekt mit der Datenbank verbinden

1. Öffnen Sie Ihr Django-Projekt in Visual Studio Code.
2. ErstellenSie eine neue Datei namens `.env` im Hauptverzeichnis des Projekts.
3. Fügen Sie die folgenden Zeilen in die `.env`-Datei ein und passen Sie die Werte entsprechend Ihrer Datenbankverbindung an:

```
DB_NAME=IhrDatenbankname
DB_USER=IhrBenutzername
DB_PASSWORD=IhrPasswort
DB_HOST=IhrHostname
DB_PORT=IhrPort
```

4. Öffnen Sie die Datei `settings.py` im Projektverzeichnis und suchen Sie nach der Zeile `DATABASES`.
5. Ändern Sie die `DATABASES`-Variable, um die Verbindungsparameter aus der `.env`-Datei zu verwenden:

```python
import os
from dotenv import load_dotenv

load_dotenv()

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.environ.get('DB_NAME'),
        'USER': os.environ.get('DB_USER'),
        'PASSWORD': os.environ.get('DB_PASSWORD'),
        'HOST': os.environ.get('DB_HOST'),
        'PORT': os.environ.get('DB_PORT'),
    }
}
```

6. Speichern Sie die Änderungen in der `settings.py`-Datei.

## Schritt 5: Datenbankmigrationen durchführen

1. Öffnen Sie eine Kommandozeile oder ein Terminal und navigieren Sie zum Verzeichnis Ihres Django-Projekts.
2. Aktivieren Sie die zuvor erstellte Anaconda-Umgebung mit dem Befehl: `conda activate myenv`.
3. Führen Sie den folgenden Befehl aus, um die vorhandenen Datenbankmigrationen anzuwenden: `python manage.py migrate`.

Wenn alle Migrationen erfolgreich angewendet wurden, ist Ihr Django-Projekt nun mit der Datenbank verbunden und einsatzbereit.

## Schritt 6: Frontend-Pakete installieren

1. Navigieren Sie zum Verzeichnis Ihres Frontend-Projekts (React, Angular oder Vue) in der Kommandozeile oder im Terminal.
2. Stellen Sie sicher, dass die zuvor installierte Node.js-Version (16) aktiviert ist, indem Sie den Befehl `nvm use 16` ausführen.
3. Führen Sie den Befehl `npm install` aus, um alle erforderlichen Frontend-Pakete zu installieren.

Sobald die Installation abgeschlossen ist, können Sie das Frontend-Projekt starten und mit dem Backend verbinden.

## Schritt 7: Frontend-Projekt starten

1. Stellen Sie sicher, dass Sie sich immer noch im Verzeichnis Ihres Frontend-Projekts befinden.
2. Führen Sie den Befehl `npm start` aus, um das Frontend-Projekt zu starten.
3. Öffnen Sie einen Webbrowser und navigieren Sie zur angegebenen Adresse, um das Frontend-Projekt anzuzeigen und zu verwenden.


## Problembehebung im Frontend
Falls Probleme im Frontend auftreten, erstellen Sie eine .env-Datei im Frontend-Verzeichnis und fügen Sie die folgende Zeile hinzu:
Copy
SKIP_PREFLIGHT_CHECK=true
Nachdem Sie diese Schritte durchgeführt haben, sollte das Django-Projekt bereit sein, sowohl im Backend als auch im Frontend verwendet zu werden. Achten Sie darauf, den Django-Entwicklungsserver laufen zu lassen, während Sie das Projekt verwenden, und stellen Sie sicher, dass Ihre MySQL-Verbindung
