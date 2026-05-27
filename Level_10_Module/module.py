# ============================================================
# EINHEIT 10: Module
# ============================================================

# ------------------------------------------------------------
# THEORIE: Was sind Module?
# ------------------------------------------------------------
# Python bringt viele nützliche Funktionen mit, die in Modulen
# organisiert sind. Module sind Sammlungen von Funktionen und
# Variablen, die thematisch zusammengehören und bei Bedarf
# eingebunden werden.
#
# Wichtige Module der Standardbibliothek:
#   random   → Zufallszahlen und -auswahlen
#   math     → mathematische Funktionen
#   datetime → Datum und Uhrzeit
#   os       → Betriebssystemzugriff
#
# Darüber hinaus gibt es externe Module die mit pip installiert
# werden können, z.B.: numpy, pandas, matplotlib, requests

# ------------------------------------------------------------
# Beispiel 1: import Varianten
# ------------------------------------------------------------

# Variante 1: Ganzes Modul importieren
import random
# print(random.randint(1, 100))

# Variante 2: Einzelne Funktionen importieren
# from random import randint
# print(randint(1, 10))

# Variante 3: Modul mit Alias importieren
# import random as rnd
# print(rnd.randint(1, 20))

# Variante 4: Alias für Funktionsnamen vergeben
# from random import randint as kartoffelbrei
# print(kartoffelbrei(1, 100))

# ----------------------------------------------------------
# BEISPIEL 2: random.random() und random.uniform()
# ----------------------------------------------------------
# random() gibt eine Kommazahl zwischen 0.0 und 1.0 zurück.
# uniform(a, b) gibt eine Kommazahl zwischen a und b zurück.

wert = random.random()
print(wert)

temperatur = random.uniform(15.0, 35.0)

print(f"Zufallswert zwischen 0.0 und 1.0: {wert}")
print(f"Zufälliger Temperaturwert: {temperatur:.2f}")

# ------------------------------------------------------------
# BEISPIEL 3: random.choice() – Zufälliges Element aus einer Liste
# ------------------------------------------------------------
# choice(liste) wählt ein zufälliges Element aus einer Liste.

fruechte = ["Apfel", "Banane", "Kirsche", "Mango"]
auswahl = random.choice(fruechte)
print(f"Zufällige Frucht: {auswahl}")

# ------------------------------------------------------------
# BEISPIEL 4: random.shuffle() und random.sample()
# ------------------------------------------------------------
# shuffle(liste) mischt die Liste direkt – die Originalliste
# wird verändert, es wird nichts zurückgegeben.
#
# sample(liste, k) gibt k zufällig gewählte eindeutige Elemente
# zurück, ohne die Originalliste zu verändern.

karten = ["Ass", "König", "Dame", "Bube", "10"]
random.shuffle(karten)
print(f"Gemischte Karten: {karten}")

zahlen = list(range(1, 50))
lottozahlen = random.sample(zahlen, 6)
print(f"Lottozahlen: {lottozahlen}")
