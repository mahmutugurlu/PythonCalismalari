# ============================================================
# EINHEIT 11: Funktionen
# ============================================================

# ------------------------------------------------------------
# THEORIE: Warum brauchen wir Funktionen?
# ------------------------------------------------------------
# Wenn dieselbe Logik an mehreren Stellen gebraucht wird,
# müsste man sie jedes Mal neu schreiben das ist fehleranfällig.
#
# Funktionen lösen das: einmal definiert, beliebig oft aufrufbar.
#   - Kein doppelter Code (DRY: Don't Repeat Yourself)
#   - Bessere Lesbarkeit: jede Funktion hat einen klaren Zweck
#   - Einfachere Fehlersuche: Fehler nur an einer Stelle beheben
#
# Syntax:
#   def funktionsname(parameter):
#       """Docstring: Was macht diese Funktion?"""
#       return ergebnis

# ------------------------------------------------------------
# BEISPIEL 1: Funktion ohne Parameter und ohne Rückgabewert
# ------------------------------------------------------------

def trennlinie():
    """Gibt eine einheitliche Trennlinie aus"""
    print("=" * 30)

trennlinie()
print("Ergebnisse")
trennlinie()
print("Highscore")
trennlinie()

# Ohne Funktion müsste print("=" * 30) dreimal geschrieben werden
# Bei einer Änderung müssten wir alle drei Stellen anpassen
# Eine Funktion löst dieses Problem

# ------------------------------------------------------------
# BEISPIEL 2: Funktion mit Parameter
# ------------------------------------------------------------
# Parameter machen Funktionen dynamisch verwendbar
# Die Funktion bekommt Werte übergeben und arbeitet mit diesen

def drucke_trennlinie(zeichen, laenge):
    """Gibt eine einheitliche Trennlinie mit wählbarem Zeichen und Länge aus"""
    print(zeichen * laenge)

drucke_trennlinie("=", 30)
drucke_trennlinie("-", 20)
drucke_trennlinie("*", 15)

# ------------------------------------------------------------
# BEISPIEL 3: Funktion mit Parameter und Rückgabewert
# ------------------------------------------------------------
# Ohne return kann eine Funktion nur etwas ausführen (wie z.B. print())
# Mit return liefert sie einen Wert zurück, der weiterverwendet werden kann

def celsius_zu_fahrenheit(celsius):
    # ergebnis = celsius * 9 / 5 + 32
    # return ergebnis
    return celsius * 9 / 5 + 32   # verkürzte Version

nutzereingabe = int(input("Bitte gib eine Temperatur in Celsius an: "))

print(f"{nutzereingabe} °C = {celsius_zu_fahrenheit(nutzereingabe)}° Fahrenheit")
print(f"100°C = {celsius_zu_fahrenheit(100)}° Fahrenheit")

# Rückgabewert in Variable speichern
fiebergrenze_in_fahrenheit = celsius_zu_fahrenheit(37)
print(f"Fieber ab: {fiebergrenze_in_fahrenheit} °F")

# ------------------------------------------------------------
# BEISPIEL 4: Standardwerte und Keyword-Argumente
# ------------------------------------------------------------
# Parameter können einen Standardwert haben (falls kein Argument übergeben wird)

def begruesse(name, anrede="Hallo"):        # anrede hat den Standardwert "Hallo"
    return f"{anrede}, {name}"

print(begruesse("Kai"))                              # Standardwert wird genutzt -> "Hallo, Kai"
print(begruesse("Kai", "Guten Tag"))    # Positionsargument: Parameter wird mit dem Namen übergeben
print(begruesse("Kai", anrede="Guten Tag"))    # Keyword-Argument: Parameter mit seinem Parmeternamen übergeben
print(begruesse(anrede="Hi", name="Kai"))            # Nur Keyword-Argumente: Reihenfolge spielt keine Rolle
print(begruesse("Anna"))

# print(begruesse(anrede="Guten Tag", "Kai"))         # Positionsargumente müssen vor Keyword-Argumenten stehen
# print(begruesse(anrede="Hi"))                       # Alle Parameter ohne Standardwert müssen gesetzt werden!

# ------------------------------------------------------------
# BEISPIEL 5: Scope - lokale und globale Variablen
# ------------------------------------------------------------
# Variablen außerhalb einer Funktion heißen global → überall lesbar
# Variablen innerhalb einer Funktion heißen lokal  → nur in der Funktion bekannt

punkte = 100            # globale Variable -> auch in Funktionen lesbar

def berechne_bonus(multiplikator):
    ergebnis = punkte * multiplikator       # lokale Variable -> nur hier in der Funktion bekannt
    return ergebnis

print(berechne_bonus(2))
print(punkte)

# print(ergebnis)    # An dieser Stelle ist für Python die Variable "ergebnis" unbekannt