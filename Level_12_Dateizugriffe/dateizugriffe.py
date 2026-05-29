# ============================================================
# EINHEIT 12: Dateizugriffe
# ============================================================

# ------------------------------------------------------------
# THEORIE: Warum brauchen wir Dateizugriffe?
# ------------------------------------------------------------
# Bisher haben unsere Programme alle Daten im Arbeitsspeicher
# gehalten - wenn das Programm beendet wird, sind alle Daten
# verloren. Mit Dateien lassen sich Daten dauerhaft
# speichern und später wieder einlesen.
#
# Anwendungsbeispiele:
#   - Notizen oder Einstellungen speichern
#   - Protokolle (Logs) schreiben
#   - Daten aus Textdateien einlesen und verarbeiten
#
# Python öffnet Dateien mit der eingebauten Funktion open().
# Syntax: open(dateipfad, modus, encoding="utf-8")
#
# Die wichtigsten Modi:
#   "r"  → read:   Datei lesen   (Datei muss existieren)
#   "w"  → write:  Datei schreiben (erstellt neu oder überschreibt)
#   "a"  → append: An bestehende Datei anhängen
#
# Durch Anhängen von "b" wird die Datei als Binärstrom geöffnet,
# z.B. für Bilder, Audio oder andere Nicht-Textdateien:
#   "rb" → Binärdatei lesen
#   "wb" → Binärdatei schreiben
# Im Binärmodus wird kein encoding angegeben, da keine
# Zeichenkodierung stattfindet.
#
# Encoding:
# Verschiedene Betriebssysteme verwenden unterschiedliche
# Zeichenkodierungen. Mit encoding="utf-8" stellen wir sicher,
# dass Sonderzeichen wie Umlaute (ä, ö, ü) auf allen Systemen
# korrekt gelesen und geschrieben werden.

# ------------------------------------------------------------
# BEISPIEL 1: Datei schreiben - Modus "w"
# ------------------------------------------------------------
# "w" erstellt eine neue Datei oder überschreibt eine bestehende vollständig.
#
# Ohne with muss die Datei manuell mit close() geschlossen werden
# Vergisst man das, kann es zu Datenverlust oder Konflikten kommen.
# Das with-Statement schließt die Datei automatisch und ist daher die empfohlene Methode.
#
# Ohne with:                    Mit with (empfohlen):
#   datei = open(...)              with open(...) as datei:
#   datei.write("Hallo")           datei.write("Hallo")
#   datei.close()                  # Automatisch geschlossen

# datei = open("notizen.txt", "w", encoding="utf-8")
# datei.write("Neuer Text")
# datei.close()

# Mit dem Öffnen folgender Datei unter dem Variablennamen "datei" tue folgendes;
with open("notizen.txt", "w", encoding="utf-8") as datei:
    datei.write("Erste Notiz: Python lernen\n")
    datei.write("Zweite Notiz: Aufgaben erledigen\n")
    datei.write("Dritte Notiz: Buch lesen\n")

print("Datei wurde geschrieben")
print()

# ------------------------------------------------------------
# BEISPIEL 2: Datei lesen - Modus "r"
# ------------------------------------------------------------
# Es gibt unterschiedliche gebräuchliche Wege, um eine Datei zu lesen:

# Variante A: for Schleife liest zeilenweise
with open("notizen.txt", "r", encoding="utf-8") as datei:
    for zeile in datei:
        # print(zeile, end="")
        print(zeile.strip())    # strip() entfernt führende und nachgestellte Whitespaces, \n ist ein Whitespace

# Variante B: readlines() liest alle Zeilen als Liste ein.
with open("notizen.txt", "r", encoding="utf-8") as datei:
    alle_zeilen = datei.readlines()
    print(f"Anzahl Zeilen: {len(alle_zeilen)}")
    print(f"Erste Zeile: {alle_zeilen[0]}")

# ------------------------------------------------------------
# BEISPIEL 3: An Datei anhängen - Modus "a"
# ------------------------------------------------------------
# "a" hängt neuen Inhalt ans Ende einer Datei
# vorhandener Inhalt bleibt erhalten

with open("notizen.txt", "a", encoding="utf-8") as datei:
    datei.write("Vierte Notiz: Sport treiben")

# ------------------------------------------------------------
# BEISPIEL 4: Fehlerbehandlung bei Dateizugriffen
# ------------------------------------------------------------
# Aus Level 09 kennen wir try/except, bei Dateizugriffen ist Fehlerbehandlung besonders wichtig
# FileNotFoundError -> Datei existiert nicht

try:
    with open("nicht_vorhanden.txt", "r", encoding="utf-8") as datei:
        inhalt = datei.read()
except FileNotFoundError:
    print("Fehler: Datei wurde nicht gefunden")

# ------------------------------------------------------------
# BEISPIEL 5: Datei lesen, verändern und neu schreiben
# ------------------------------------------------------------

# Alle Zeilen einlesen (als Liste)
with open("notizen.txt", "r", encoding="utf-8") as datei:
    zeilen = datei.readlines()

# Jede Zeile nummerieren:
nummeriert = []
for zeile in range(len(zeilen)):
    nummeriert.append(f"{zeile + 1} {zeilen[zeile]}")

print(nummeriert)

# Ergebnis in neue Datei schreiben
# with open("notizen_nummeriert.txt", "w", encoding="utf-8") as datei:
#     datei.writelines(nummeriert)

# Relativer Pfad: bezieht sich auf den aktuellen Ordner
# Absoluter Pfad vollständige Pfad zur Datei

with open("../notizen_nummeriert.txt", "w", encoding="utf-8") as datei:
    # for zeile in range(len(zeilen)):
    #     datei.write(nummeriert[zeile])
    datei.writelines(nummeriert)

with open("C:/Users/maximilian.ferres/OneDrive - Amadeus Fire AG/Dokumente/notizen_nummeriert.txt", "w", encoding="utf-8") as datei:
    # for zeile in range(len(zeilen)):
    #     datei.write(nummeriert[zeile])
    datei.writelines(nummeriert)