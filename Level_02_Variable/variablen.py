# ============================================================
# EINHEIT 02: Variablen und Datentypen
# ============================================================

# ------------------------------------------------------------
# THEORIE: Was ist eine Variable?
# ------------------------------------------------------------
# Stell dir eine Reihe Spinde vor, wie im Fitnessstudio oder in der alten Schule.
# Jeder Spind hat ein Namensschild drauf.
# Du öffnest nicht Spind Nr. 4872, sondern einfach "Tom's Spind".
# Der Inhalt steckt dahinter, die Nummer interessiert dich nicht.
#
# Genauso funktioniert eine Variable in Python:
# Statt einer Spindnummer bekommt ein Speicherplatz im Arbeitsspeicher einen Namen.
# Python reserviert intern eine Adresse im RAM und merkt sich, dass unser
# Variablenname auf genau diese Adresse zeigt, wir müssen uns darum nicht kümmern,
# Python erledigt das für uns. Wir arbeiten immer nur mit dem Namen.
#
# Syntax: variablenname = wert
#
# Das = ist kein mathematisches Gleichheitszeichen, sondern
# ein Zuweisungsoperator: "Speichere diesen Wert unter diesem Namen."

# ------------------------------------------------------------
# 1. Variablen erstellen und anwenden
# ------------------------------------------------------------

name = "Maximilian"         # Variable "name" speichert den String "Maximilian"
print(name)                 # Gibt den Inhalt der Variablen aus
alter = 33                  # Variable "zahl" speichert die Zahl 33
print(alter)

# Wir können den Wert eine Variablen überschreiben
name = "Hans Peter"         # Variable wird überschrieben / neuer Wert zugewiesen
print(name)

# Mehrfachzuweisung geht auch!
zahl1, zahl2, zahl3 = 5, 10, 15
zahl1 = 5
zahl2 = 10
zahl3 = 15
print(zahl1, zahl2, zahl3)

# ------------------------------------------------------------
# THEORIE: Regeln für Variablennamen
# ------------------------------------------------------------
# Gute Variablennamen machen Code lesbar. Die Regeln:
#   ✓ Darf Buchstaben, Zahlen und _ enthalten
#   ✓ Muss mit einem Buchstaben oder _ beginnen
#   ✗ Darf keine Leerzeichen oder Sonderzeichen enthalten
#   ✗ Darf kein reserviertes Python-Schlüsselwort sein (if, for, while ...)
#   ✗ Groß- und Kleinschreibung wird unterschieden (name ≠ Name ≠ NAME)
#
# Konvention: snake_case – Wörter mit Unterstrich trennen

# Gut:
kunden_name = "Tom"         # Unterstrich als Trennzeichen (snake_case)
BILDSCHIRM_BREITE = 1920    # Konstante in Großbuchstaben
punkte2 = 50                # Zahlen erlaubt, solange sie nicht am Anfang stehen
_punktzahl = 99             # Unterstrich am Anfang erlaubt

# Schlecht:
x = "Tom"                   # Nichtsaussagend, was ist x?
aaaa = 50                   # kein erkennbarer Sinn
SpielerName = "Tom"         # Pascal Case in Python unüblich, besser snake_case
                            # In anderen Sprachen CamelCase Beispiel: spielerName

# ------------------------------------------------------------
# 2. Die vier grundlegenden Datentypen im Überblick
# ------------------------------------------------------------
# Python unterscheidet, welche Art von Wert in einer Variable steckt.
# Unterschiedliche Werte werden im Speicher unterschiedlich abgelegt:
# Eine ganze Zahl belegt weniger Platz als eine Kommazahl, und Text
# wird grundlegend anders kodiert als eine Zahl.
#
#   int   → ganze Zahlen          z.B. 42, -7, 0
#   float → Kommazahlen           z.B. 3.14, -0.5, 2.0
#   str   → Text (String)         z.B. "Hallo", "42", ""
#   bool  → Wahrheitswert         z.B. True, False

punkte = 100                  # int - ganze Zahl, positive und negative Zahlen sind möglich
durchschnitt = 87.5           # float - Fließkommazahl
spieler_name = "xXDarkLordXx" # str - Text in Anführungszeichen
hat_gewonnen = True           # bool - True oder False

# ------------------------------------------------------------
# 3. type() - Den Datentyp abfragen
# ------------------------------------------------------------
# Mit type() kann Python uns sagen, welchen Typ ein Wert hat
#
# type() verhält sich anders als print():
#   print() zeigt etwas an, es gibt nichts zurück, es handelt einfach.
#   type()  gibt einen Wert zurück, wie ein Taschenrechner, der ein Ergebnis liefert.

datentyp = type(punkte)         # Den Rückgabewert von type() in einer Variablen speichern
print("Datentyp:", datentyp)

# Neben normalen Werten oder Variablen Funktionen im print() Befehl verwenden
# Python führt zuerst die Funktion type() aus und gibt das Ergebnis an den print() Befehl zurück
print("Datentyp:", type(punkte))
# print("Datentyp:", "<class 'int'>")

# Achtung !
zahl_als_text = "42"
print(type(zahl_als_text))
# print(zahl_als_text + 5)
# Python kann nicht mit Text rechnen

# ------------------------------------------------------------
# 4. Variablen verändern und aktualisieren
# ------------------------------------------------------------
# Eine Variable kann auf ihren eigenen alten Wert zurückgreifen
# Zum Beispiel, wenn man in Programmen einen Zähler erhöhen möchte

leben = 3
print("Leben:", leben)
leben = leben - 1       # leben = 3 - 1
print("Leben:", leben)

# Kurzschreibweisen
punkte = 0
punkte += 10        # punkte = punkte + 10
print("Punktzahl:", punkte)

punkte *= 2
print("Punktzahl:", punkte)

punkte /= 10
print("Punktzahl:", punkte)

# weitere -=, /=, //=, %=

