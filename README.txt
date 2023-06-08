# Django-Projekt mit Anaconda
------------------------------

Dieses Django-Projekt wurde mit Anaconda erstellt und enthält eine `requirements.txt`-Datei, die alle erforderlichen Pakete und Bibliotheken für das Projekt auflistet.

## Installation von Anaconda

1. Laden Sie die Installationsdatei von der [Anaconda-Website](https://www.anaconda.com/products/distribution) herunter, die für Ihr Betriebssystem geeignet ist.
2. Öffnen Sie die Installationsdatei und folgen Sie den Anweisungen auf dem Bildschirm, um Anaconda auf Ihrem System zu installieren.

## Verwendung von Anaconda

1. Öffnen Sie eine Kommandozeile oder ein Terminal und navigieren Sie zu dem Verzeichnis, in dem das Django-Projekt gespeichert ist. Verwenden Sie dazu den Befehl `cd "../team01/Backend"`.

2. Erstellen Sie eine neue Umgebung in Anaconda mit dem Befehl: `conda create -n myenv python=3.8`.

3. Aktivieren Sie die neue Umgebung mit dem Befehl: `conda activate myenv`.

4. Installieren Sie Django in dieser Umgebung mit dem Befehl: `conda install django`.

5. Installieren Sie alle erforderlichen Pakete und Bibliotheken aus der `requirements.txt`-Datei mit dem Befehl: `pip install -r requirements.txt`.

## Installation von nvm (Node Version Manager) für Windows

1. Laden Sie die `nvm-setup.exe`-Datei aus dem Ordner `\team01\Node installation` herunter oder besuchen Sie diesen [Link](https://github.com/coreybutler/nvm-windows/releases), um die neueste Version von nvm für Windows herunterzuladen.
2. Führen Sie die heruntergeladene `nvm-setup.exe`-Datei aus und folgen Sie den Anweisungen auf dem Bildschirm, um nvm auf Ihrem System zu installieren.

### Installation von Node.js

1. Öffnen Sie eine Kommandozeile oder ein Terminal und führen Sie den Befehl `nvm install 16` aus, um Node.js Version 16 zu installieren.

2. Führen Sie den Befehl `nvm use 16` aus, um die installierte Node.js-Version zu verwenden.

Nach der Installation von Anaconda und nvm können Sie mit den folgenden Schritten fortfahren.

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

1. Öffnen Sie das Django-Projekt "Backend" in Visual Studio Code.
2. Erstellen Sie eine neue Datei namens `.env` im Hauptverzeichnis des Projekts.
3. Fügen Sie die folgenden Zeilen in die `.env`-Datei ein und passen Sie die Werte entsprechend Ihrer Datenbankverbindung an:

```
DB_NAME=dongle1
DB_USER=IhrBenutzername
DB_PASSWORD=IhrPasswort
DB_HOST=localhost
DB_PORT=3306
```
6. Speichern Sie die Änderungen.

## Schritt 6: Frontend-Pakete installieren und ausführen

1. Öffnen Sie ein Terminal oder eine Kommandozeile und navigieren Sie zum Frontend-Verzeichnis des Projekts mit dem Befehl `cd "../team01/Frontend"`.

2. Führen Sie den Befehl `npm install` aus, um alle erforderlichen Pakete für das Frontend zu installieren.

3. Führen Sie den Befehl `npm start` aus, um das Frontend zu starten. Die Anwendung sollte nun im Browser unter `http://localhost:3000` erreichbar sein.

## Schritt 7: Django-Server ausführen

1. Öffnen Sie ein neues Terminal oder eine Kommandozeile und navigieren Sie zum Backend-Verzeichnis des Projekts mit dem Befehl `cd "../team01/Backend"`.

2. Stellen Sie sicher, dass Sie die Anaconda-Umgebung, die Sie zuvor erstellt haben, aktiviert haben. Wenn nicht, führen Sie den Befehl `conda activate myenv` aus.

3. Führen Sie den Befehl `python manage.py runserver` aus, um den Django-Server zu starten. Der Server sollte nun unter `http://localhost:8000` erreichbar sein.

Jetzt sollten sowohl das Frontend als auch das Backend laufen, und Sie können die Anwendung in Ihrem Browser verwenden. Wenn Sie auf Probleme stoßen oder weitere Unterstützung benötigen, zögern Sie nicht, uns zu kontaktieren.