# ============================================================
# EINHEIT 9: Fehlerbehandlung
# ============================================================

# ------------------------------------------------------------
# THEORIE: Was sind Ausnahmen?
# ------------------------------------------------------------
# Bisher sind unsere Programme bei einem Fehler einfach abgestürzt.
# In echten Programmen ist das inakzeptabel.
#
# Python unterscheidet zwei Arten von Fehlern:
#   Syntaxfehler  → Fehler im Code selbst, werden vor der Ausführung
#                   erkannt (z.B. fehlende Klammer, Tippfehler)
#   Ausnahmen     → Fehler zur Laufzeit, also während das Programm
#                   läuft (z.B. Division durch 0, falsche Eingabe)
#
# Ausnahmen lassen sich abfangen und behandeln
# Das Programm läuft dann kontrolliert weiter, anstatt abzustürzen.
#
# Häufige Ausnahmen:
#   ValueError        → falscher Wert (z.B. int("abc"))
#   ZeroDivisionError → Division durch 0
#   IndexError        → Index außerhalb der Liste
#   TypeError         → falscher Typ (z.B. "2" + 2)
#   FileNotFoundError → Datei nicht gefunden

# ------------------------------------------------------------
# BEISPIEL 1: try / except – Grundprinzip
# ------------------------------------------------------------
# Der try-Block enthält Code, der einen Fehler auslösen könnte.
# Tritt ein Fehler auf, springt Python in den except-Block.
# Tritt kein Fehler auf, wird except übersprungen.
#
# Mit "as e" lässt sich die originale Fehlermeldung ausgeben –
# das ist besonders beim Debuggen hilfreich.

try:  # Hier steht der Code wo Fehler entstehen könnten
    zahl = int(input("Gib eine ganze Zahl ein: "))
    print(f"Du hast {zahl} eingegeben")
except ValueError as err:  # Hier steht was passiert, wenn ein Fehler ausgelöst wurde
    print(f"Fehler: Das war keine gültige Zahl! {err}")

print("Das Programm läuft weiter")

# ------------------------------------------------------------
# BEISPIEL 2: Mehrere except Blöcke
# ------------------------------------------------------------
# Verschiedene Fehlertypen können unterschiedlich behandelt werden
# Python prüft die except Blöcke von oben nach unten und führt den ersten passenden Block aus

try:
    a = int(input("Erste Zahl eingeben: "))
    b = int(input("Zweite Zahl eingeben: "))
    ergebnis = a / b
    print(f"Ergebnis: {ergebnis}")
except ValueError:
    print("Bitte nur ganze Zahlen eingeben!")
except ZeroDivisionError:
    print("Fehler: Division durch 0 ist nicht erlaubt!")

# ------------------------------------------------------------
# BEISPIEL 3: Eingabeschleife mit Fehlerbehandlung
# ------------------------------------------------------------
# Ein häufiges Muster: So lange Fragen, bis eine gültige Eingabe kommt

# Der finally Block wird IMMER ausgeführt, egal ob ein Fehler aufgetreten ist oder nicht
# Er eignet sich weitere Meldungen oder Aufräumarbeiten, die in jedem Fall stattfinden müssen

while True:
    try:
        alter = int(input("Alter eingeben (1-122):"))
        if alter < 1 or alter > 122:
            print("Ungültige Eingabe: Alter muss zwischen 1 und 122 liegen")
        else:
            print(f"Alter akzeptiert: {alter}")
            break
    except ValueError as e:
        print(f"Ungültige Eingabe: Das war keine Zahl! {e}")
