# Team01

## Getting started

To make it easy for you to get started with GitLab, here's a list of recommended next steps.

Already a pro? Just edit this README.md and make it your own. Want to make it easy? [Use the template at the bottom](#editing-this-readme)!

## Add your files

- [ ] [Create](https://docs.gitlab.com/ee/user/project/repository/web_editor.html#create-a-file) or [upload](https://docs.gitlab.com/ee/user/project/repository/web_editor.html#upload-a-file) files
- [ ] [Add files using the command line](https://docs.gitlab.com/ee/gitlab-basics/add-file.html#add-a-file-using-the-command-line) or push an existing Git repository with the following command:

```
cd existing_repo
git remote add origin https://gitlab.rz.htw-berlin.de/softwareentwicklungsprojekt/sose2023/team01.git
git branch -M main
git push -uf origin main
```

## Integrate with your tools

- [ ] [Set up project integrations](https://gitlab.rz.htw-berlin.de/softwareentwicklungsprojekt/sose2023/team01/-/settings/integrations)

## Collaborate with your team

- [ ] [Invite team members and collaborators](https://docs.gitlab.com/ee/user/project/members/)
- [ ] [Create a new merge request](https://docs.gitlab.com/ee/user/project/merge_requests/creating_merge_requests.html)
- [ ] [Automatically close issues from merge requests](https://docs.gitlab.com/ee/user/project/issues/managing_issues.html#closing-issues-automatically)
- [ ] [Enable merge request approvals](https://docs.gitlab.com/ee/user/project/merge_requests/approvals/)
- [ ] [Automatically merge when pipeline succeeds](https://docs.gitlab.com/ee/user/project/merge_requests/merge_when_pipeline_succeeds.html)

## Test and Deploy

Use the built-in continuous integration in GitLab.

- [ ] [Get started with GitLab CI/CD](https://docs.gitlab.com/ee/ci/quick_start/index.html)
- [ ] [Analyze your code for known vulnerabilities with Static Application Security Testing(SAST)](https://docs.gitlab.com/ee/user/application_security/sast/)
- [ ] [Deploy to Kubernetes, Amazon EC2, or Amazon ECS using Auto Deploy](https://docs.gitlab.com/ee/topics/autodevops/requirements.html)
- [ ] [Use pull-based deployments for improved Kubernetes management](https://docs.gitlab.com/ee/user/clusters/agent/)
- [ ] [Set up protected environments](https://docs.gitlab.com/ee/ci/environments/protected_environments.html)

---

# Editing this README

When you're ready to make this README your own, just edit this file and use the handy template below (or feel free to structure it however you want - this is just a starting point!). Thank you to [makeareadme.com](https://www.makeareadme.com/) for this template.

## Suggestions for a good README

Every project is different, so consider which of these sections apply to yours. The sections used in the template are suggestions for most open source projects. Also keep in mind that while a README can be too long and detailed, too long is better than too short. If you think your README is too long, consider utilizing another form of documentation rather than cutting out information.

## Name

Choose a self-explaining name for your project.

## Description

Let people know what your project can do specifically. Provide context and add a link to any reference visitors might be unfamiliar with. A list of Features or a Background subsection can also be added here. If there are alternatives to your project, this is a good place to list differentiating factors.

## Badges

On some READMEs, you may see small images that convey metadata, such as whether or not all the tests are passing for the project. You can use Shields to add some to your README. Many services also have instructions for adding a badge.

## Visuals

Depending on what you are making, it can be a good idea to include screenshots or even a video (you'll frequently see GIFs rather than actual videos). Tools like ttygif can help, but check out Asciinema for a more sophisticated method.

## Installation

Wenn Sie das Projekt zum ersten Mal verwenden, befolgen Sie die Anweisungen von Anfang an. Wenn Sie bereits alles installiert haben, springen Sie zum Abschnitt "Bereits installiert" weiter unten.

# Django-Projekt mit Anaconda

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

## Schritt 5: Frontend-Pakete installieren und ausführen

1. Öffnen Sie ein Terminal oder eine Kommandozeile und navigieren Sie zum Frontend-Verzeichnis des Projekts mit dem Befehl `cd "../team01/Frontend"`.

2. Führen Sie den Befehl `npm install` aus, um alle erforderlichen Pakete für das Frontend zu installieren.

3. Führen Sie den Befehl `npm start` aus, um das Frontend zu starten. Die Anwendung sollte nun im Browser unter `http://localhost:3000` erreichbar sein.

## Schritt 6: Django-Server ausführen

1. Öffnen Sie ein neues Terminal oder eine Kommandozeile und navigieren Sie zum Backend-Verzeichnis des Projekts mit dem Befehl `cd "../team01/Backend"`.

2. Stellen Sie sicher, dass Sie die Anaconda-Umgebung, die Sie zuvor erstellt haben, aktiviert haben. Wenn nicht, führen Sie den Befehl `conda activate myenv` aus.

3. Führen Sie den Befehl `python manage.py runserver` aus, um den Django-Server zu starten. Der Server sollte nun unter `http://localhost:8000` erreichbar sein.

Jetzt sollten sowohl das Frontend als auch das Backend laufen, und Sie können die Anwendung in Ihrem Browser verwenden. Wenn Sie auf Probleme stoßen oder weitere Unterstützung benötigen, zögern Sie nicht, uns zu kontaktieren.

## Bereits installiert

Wenn Sie bereits alles installiert haben, führen Sie die folgenden Schritte aus:

1. Navigieren Sie zum Ordner des Projekts: ...\team01>.

2. Installieren Sie die neuen Node-Module mit dem Befehl: "npm install".

3. Fügen Sie die benötigten Bibliotheken für das Backend hinzu, indem Sie den Befehl "pip freeze > requirements.txt" ausführen.

4. Starten Sie das Projekt mit dem Befehl "npm start".

Hier sind einige Konten, die Sie zum Testen der Anwendung verwenden können:

Admin-Konto(Superuser):
E-Mail: admin@example.com
Passwort: testpassword

Admin-Konto:
E-Mail: newuser@example.com
Passwort: testpassword

Verwalter-Konto:
E-Mail: houssemhfassa25@gmail.com
Passwort: testpassword

Kunden-Konto:
E-Mail: kundeuser@example.com
Passwort: testpassword

Verwenden Sie diese Anmeldedaten, um die verschiedenen Rollen und Funktionen innerhalb der Anwendung zu testen. Wenn Sie auf Probleme stoßen oder weitere Unterstützung benötigen, zögern Sie nicht, uns zu kontaktieren.

## Usage

Use examples liberally, and show the expected output if you can. It's helpful to have inline the smallest example of usage that you can demonstrate, while providing links to more sophisticated examples if they are too long to reasonably include in the README.

## Support

Tell people where they can go to for help. It can be any combination of an issue tracker, a chat room, an email address, etc.

## Roadmap

If you have ideas for releases in the future, it is a good idea to list them in the README.

## Contributing

State if you are open to contributions and what your requirements are for accepting them.

For people who want to make changes to your project, it's helpful to have some documentation on how to get started. Perhaps there is a script that they should run or some environment variables that they need to set. Make these steps explicit. These instructions could also be useful to your future self.

You can also document commands to lint the code or run tests. These steps help to ensure high code quality and reduce the likelihood that the changes inadvertently break something. Having instructions for running tests is especially helpful if it requires external setup, such as starting a Selenium server for testing in a browser.

## Authors and acknowledgment

Show your appreciation to those who have contributed to the project.

## License

Copyright (c) 2023 HTW Berlin Softwareentwicklung Gruppe 1 (Rama Abazied, Yassin Sahnoun, Houssem Hfasa)

Hiermit wird jeder Person, die eine Kopie dieser Software und der zugehörigen Dokumentationsdateien (die "Software") erhält, die Erlaubnis erteilt, kostenlos und ohne Einschränkungen mit der Software zu handeln. Dies umfasst die Rechte zur Nutzung, zum Kopieren, Ändern, Zusammenführen, Veröffentlichen, Verteilen, Unterlizenzieren und/oder Verkaufen von Kopien der Software.

Die folgenden Bedingungen müssen erfüllt sein, um diese Erlaubnis zu erhalten:

Der oben genannte Urheberrechtshinweis und dieser Genehmigungshinweis müssen in allen Kopien oder wesentlichen Teilen der Software enthalten sein.

DIE SOFTWARE WIRD "WIE SIE IST" UND OHNE JEGLICHE AUSDRÜCKLICHE ODER STILLSCHWEIGENDE GEWÄHRLEISTUNG BEREITGESTELLT. DIES BEINHALTET, ABER IST NICHT BESCHRÄNKT AUF, GEWÄHRLEISTUNGEN DER MARKTGÄNGIGKEIT, EIGNUNG FÜR EINEN BESTIMMTEN ZWECK UND NICHTVERLETZUNG VON RECHTEN DRITTER. IN KEINEM FALL SIND DIE URHEBER ODER URHEBERRECHTSINHABER HAFTBAR FÜR ANSPRÜCHE, SCHÄDEN ODER ANDERE VERBINDLICHKEITEN, OB IN EINER VERTRAGS- ODER HAFTUNGSKLAGE, EINER UNERLAUBTEN HANDLUNG ODER ANDERWEITIG, DIE SICH AUS, AUS ODER IN VERBINDUNG MIT DER SOFTWARE ODER DER NUTZUNG ODER ANDEREN HANDLUNGEN MIT DER SOFTWARE ERGEBEN.

Diese Software ist Open Source und wird unter der GPLv3-Lizenz vergeben.

## Project status

If you have run out of energy or time for your project, put a note at the top of the README saying that development has slowed down or stopped completely. Someone may choose to fork your project or volunteer to step in as a maintainer or owner, allowing your project to keep going. You can also make an explicit request for maintainers.
