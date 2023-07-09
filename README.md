# Lizenzverwaltungssystem

Eine Webanwendung zur Verwaltung von Softwarelizenzen, die es Benutzern ermöglicht, Lizenzen und Dongles anzufordern, hinzuzufügen und zu verwalten, sowie Benachrichtigungen für ablaufende Lizenzen zu versenden.

## Inhaltsverzeichnis

- [Einführung](#einführung)
- [Funktionen](#funktionen)
- [Technischer Stack](#technischer-stack)
- [Systemanforderungen](#systemanforderungen)
- [Installation](#installation)
- [Verwendung](#verwendung)
- [Dokumentation](#dokumentation)
- [Beitragen](#beitragen)
- [Lizenz](#lizenz)

## Einführung

Das Lizenzverwaltungssystem ist eine Webanwendung, die entwickelt wurde, um die Verwaltung von Softwarelizenzen und Dongles zu vereinfachen und zu standardisieren. Es löst das Problem der unübersichtlichen und ineffizienten Verwaltung von Lizenzen in Form von Excel-Tabellen, indem es eine zentralisierte Plattform bietet und automatisierte Prozesse einführt.

Die Hauptmotivation hinter der Entwicklung dieses Systems ist die Optimierung von Arbeitsabläufen zur Registrierung und Verwaltung von Dongles und Lizenzen. Es ermöglicht eine automatische Benachrichtigung, wenn Dongles oder Lizenzen ablaufen, wodurch manuelles Überwachen und Erinnern überflüssig wird. Zusätzlich führt das System eine automatische Protokollierung zur Dokumentation ein, um die Transparenz und Nachvollziehbarkeit der Lizenzverwaltung zu verbessern.

## Funktionen

Listen Sie die Hauptfunktionen und Funktionen Ihrer Anwendung auf.

## Technischer Stack

Geben Sie einen Überblick über die in Ihrem Projekt verwendeten Technologien:

- Frontend: React
- Backend: Django
- Datenbank: MySQL
- Pakete: Django Rest Framework, rest_framework_simplejwt, corsheaders, dotenv, Celery, Redis, SendinBlue SMTP

## Systemanforderungen

Um die Webanwendung zur Verwaltung von Softwarelizenzen und Dongles reibungslos auszuführen, sind die folgenden Systemanforderungen zu beachten:

Betriebssystem;

Windows 10, macOS 10.14 (Mojave) oder höher, Linux (Ubuntu 18.04 oder höher)

Software;

Webbrowser: Google Chrome (Version 90 oder höher), Mozilla Firefox (Version 85 oder höher), Safari (Version 12 oder höher), Microsoft Edge (Version 85 oder höher)
Datenbank: MySQL 5.7 oder höher, PostgreSQL 10 oder höher
Backend: Python 3.7 oder höher, Django 3.2 oder höher
Frontend: Node.js 12, 14 oder 16, npm 6 oder höher, React 17 oder höher
Entwicklungsumgebung: Visual Studio Code 1.50 oder höher
Python-Distribution: Anaconda 2020.11 oder höher

Hardwareanforderungen:

Prozessor: 1 GHz oder schneller, 64-Bit-Prozessor (Dual-Core oder besser empfohlen)
Arbeitsspeicher (RAM): Mindestens 2 GB (4 GB oder mehr empfohlen)
Festplattenspeicher: Mindestens 10 GB freier Speicherplatz für die Installation und Betrieb der Anwendung, sowie zusätzlicher Speicherplatz für Backups und zukünftige Updates
Netzwerk: Breitband-Internetverbindung für den Zugriff auf die Webanwendung und die Kommunikation mit der Datenbank

## Installation

## Bereits installiert

Wenn Sie bereits alles installiert haben, führen Sie die folgenden Schritte aus:

1. Öffnen Sie eine Kommandozeile oder ein Terminal und navigieren Sie zum Ordner des Projekts: `...\team01>`.

2. Installieren Sie die neuen Node-Module mit dem Befehl: `npm install`.

3. Fügen Sie die benötigten Bibliotheken für das Backend hinzu, indem Sie den Befehl `pip install -r requirements.txt` ausführen.

4. Starten Sie das Projekt mit dem Befehl `npm start`.

## Alternative Schritte, wenn es nicht funktioniert

1. Öffnen Sie eine Kommandozeile oder ein Terminal und navigieren Sie zu dem Verzeichnis, in dem das Django-Projekt gespeichert ist. Verwenden Sie dazu den Befehl `cd "../team01/Backend"`.

2. Installieren Sie alle erforderlichen Pakete und Bibliotheken aus der `requirements.txt`-Datei mit dem Befehl: `pip install -r requirements.txt`.

3. Starten Sie das Backend mit dem Befehl `python manage.py runserver`.

4. Öffnen Sie eine neue Kommandozeile oder ein Terminal und navigieren Sie zu dem Verzeichnis, in dem das React-Frontend gespeichert ist. Verwenden Sie dazu den Befehl `cd "../team01/dongleverwaltungswebanwedung_frontend"`.

5. Installieren Sie die neuen Node-Module mit dem Befehl: `npm install`.

6. Starten Sie das Frontend mit dem Befehl `npm start`.

## Testkonto

Hier sind einige Konten, die Sie zum Testen der Anwendung verwenden können:

Admin-Konto(Superuser):
E-Mail: admin@example.com
Passwort: testpassword

Admin-Konto:
E-Mail: hgajhbdad@gmail.com
Passwort: testpassword

Verwalter-Konto:
E-Mail: newuser@example.com
Passwort: testpassword

Kunden-Konto:
E-Mail: kundeuser@example.com
Passwort: testpassword

Verwenden Sie diese Anmeldedaten, um die verschiedenen Rollen und Funktionen innerhalb der Anwendung zu testen.

# Django-Projekt mit Anaconda

Dieses Django-Projekt wurde mit Anaconda erstellt und enthält eine `requirements.txt`-Datei, die alle erforderlichen Pakete und Bibliotheken für das Projekt auflistet.

## Python-Installation

Stellen Sie sicher, dass Python auf Ihrem Computer installiert ist. Wenn nicht, befolgen Sie diese Schritte, um Python herunterzuladen und zu installieren:

1. Besuchen Sie die offizielle Python-Website ↗.
2. Laden Sie die neueste Python-Version für Ihr Betriebssystem herunter.
3. Öffnen Sie die Installationsdatei und folgen Sie den Anweisungen auf dem Bildschirm, um Python auf Ihrem System zu installieren. Stellen Sie sicher, dass Sie während der Installation die Option "Add Python to PATH" aktivieren.

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

## Schritt 5: Führen Sie das Projekt aus

Wenn Sie bereits alles installiert haben und sich in diesem Schritt befinden, folgen Sie bitte den Schritten im Abschnitt "Bereits installiert", um das Projekt (sowohl das Frontend als auch das Backend) zu starten.

## Verwendung

Die Webanwendung zur Verwaltung von Softwarelizenzen und Dongles ermöglicht den Benutzern, ihre Dongles und Lizenzen einzusehen, Anfragen zu stellen und ihre Konten zu verwalten. Die Interaktion mit der Anwendung unterscheidet sich je nach Benutzerrolle: Kunde, Verwalter oder Administrator. Im Folgenden werden die Funktionen und Interaktionen für jede Rolle beschrieben.

Kunde:

Dongles und Lizenzen ansehen: Kunden können ihre vorhandenen Dongles und Lizenzen in einer übersichtlichen Liste einsehen. In dieser Liste werden Informationen wie Produktname, Lizenztyp, Ablaufdatum und Dongle-Status angezeigt.

Dongle oder Lizenz anfordern: Kunden können über ein einfaches Formular neue Dongles oder Lizenzen anfordern. Sie müssen die erforderlichen Informationen wie Produkt, Lizenztyp und gewünschte Menge angeben und die Anfrage absenden.

Verwalter:

Dongles und Lizenzen aller Kunden einsehen: Verwalter können die Dongles und Lizenzen aller Kunden in einer zentralen Übersicht einsehen. Sie können nach Kunden oder Produkten filtern, um bestimmte Informationen schneller zu finden.

Kundenanfragen bearbeiten: Verwalter können die Anfragen von Kunden für neue Dongles oder Lizenzen einsehen und diese entweder annehmen oder ablehnen. Je nach Entscheidung werden die entsprechenden Dongles oder Lizenzen erstellt und den Kunden zugewiesen bzw. die Ablehnung kommuniziert.

Administrator:

Alle Funktionen eines Verwalters: Administratoren haben Zugriff auf alle Funktionen, die auch Verwalter ausführen können. Dazu gehört das Einsehen der Dongles und Lizenzen aller Kunden sowie das Bearbeiten von Kundenanfragen.

Nutzerliste verwalten: Administratoren können die Liste der Nutzer (Kunden, Verwalter und Administratoren) einsehen, Nutzerkonten löschen und die Rolle von Nutzern zwischen Administrator und Verwalter ändern.

Neue Konten erstellen: Administratoren können neue Nutzerkonten erstellen und die entsprechenden Rollen (Kunde, Verwalter oder Administrator) zuweisen.

Allgemeine Funktionen:

Passwort ändern: Alle Benutzer können ihr Passwort ändern, indem sie die entsprechende Funktion in ihrem Profilbereich nutzen.

Passwort zurücksetzen: Sollte ein Benutzer sein Passwort vergessen haben, kann er über die "Passwort vergessen?"-Funktion auf der Login-Seite ein neues Passwort anfordern.

## Dokumentation

Verlinken Sie zusätzliche Dokumentation oder Benutzerhandbücher.

## Beitragen

Erläutern Sie, wie andere zum Projekt beitragen, Probleme melden oder Verbesserungen vorschlagen können.

## Lizenz

Copyright (c) 2023 HTW Berlin Softwareentwicklung Gruppe 1 (Rama Abazied, Yassin Sahnoun, Houssem Hfasa)

MIT-Lizenz

Hiermit wird jeder Person, die eine Kopie dieser Software und der zugehörigen Dokumentationsdateien (die "Software") erhält, die Erlaubnis erteilt, kostenlos und ohne Einschränkungen mit der Software zu handeln. Dies umfasst die Rechte zur Nutzung, zum Kopieren, Ändern, Zusammenführen, Veröffentlichen, Verteilen, Unterlizenzieren und/oder Verkaufen von Kopien der Software.

Die folgenden Bedingungen müssen erfüllt sein, um diese Erlaubnis zu erhalten:

Der oben genannte Urheberrechtshinweis und dieser Genehmigungshinweis müssen in allen Kopien oder wesentlichen Teilen der Software enthalten sein.

DIE SOFTWARE WIRD "WIE SIE IST" UND OHNE JEGLICHE AUSDRÜCKLICHE ODER STILLSCHWEIGENDE GEWÄHRLEISTUNG BEREITGESTELLT. DIES BEINHALTET, ABER IST NICHT BESCHRÄNKT AUF, GEWÄHRLEISTUNGEN DER MARKTGÄNGIGKEIT, EIGNUNG FÜR EINEN BESTIMMTEN ZWECK UND NICHTVERLETZUNG VON RECHTEN DRITTER. IN KEINEM FALL SIND DIE URHEBER ODER URHEBERRECHTSINHABER HAFTBAR FÜR ANSPRÜCHE, SCHÄDEN ODER ANDERE VERBINDLICHKEITEN, OB IN EINER VERTRAGS- ODER HAFTUNGSKLAGE, EINER UNERLAUBTEN HANDLUNG ODER ANDERWEITIG, DIE SICH AUS, AUS ODER IN VERBINDUNG MIT DER SOFTWARE ODER DER NUTZUNG ODER ANDEREN HANDLUNGEN MIT DER SOFTWARE ERGEBEN.

Diese Software ist Open Source und wird unter der MIT-Lizenz vergeben.
