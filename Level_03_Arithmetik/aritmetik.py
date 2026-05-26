# ------------------------------------------------------------
# THEORIE: Was sind arithmetische Operatoren?
# ------------------------------------------------------------
# Arithmetische Operatoren werden verwendet, um mit Zahlen zu rechnen.
# Python kennt alle Grundrechenarten und einige zusätzliche Operatoren,
# die in der Programmierung besonders nützlich sind.
#
# Übersicht:
#   +   Addition
#   -   Subtraktion
#   *   Multiplikation
#   /   Division          → Ergebnis ist IMMER eine Fließkommazahl (float)
#   //  Ganzzahl-Division → Ergebnis wird auf die nächste ganze Zahl abgerundet
#   %   Modulo            → gibt nur den Rest einer Division zurück
#   **  Potenz            → z.B. 2 ** 3 = 8 (2 hoch 3)

# ------------------------------------------------------------
# 1. Die Grundoperatoren im Überblick
# ------------------------------------------------------------

a = 10
b = 3

print("Addition: ", a + b)
print("Subtraktion: ", a - b)
print("Multiplikation: ", a * b)
print("Division: ", a / b)              # Immer float
print("Ganzzahl-Division: ", a // b)    # 3 abgerundet, bleibt der ursprüngliche Datentyp behalten
print("Modulo: ", a % b)                # 1 (Restwert von 10 / 3)
print("Exponent", 10 ** 3)

print()

# ------------------------------------------------------------
# 2. Modulo - wozu braucht man den Rest?
# ------------------------------------------------------------
# % ist nützlich, typische Anwendungen:
# Prüfen ob eine Zahl gerade oder ungerade ist

zahl = 17
print(zahl % 2)             # 1 -> ungerade Zahl (Rest 1)

zahl = 20
print(zahl % 2)             # 0 -> gerade Zahl (kein Rest)

# Letzte Ziffer eine Zahl bestimmen
zahl = 2026
letzte_ziffer = zahl % 10
print("Letzte Ziffer:", letzte_ziffer)

# ------------------------------------------------------------
# 3. Rechnen mit Variablen
# ------------------------------------------------------------

preis = 2.50
anzahl = 4
gesamtpreis = preis * anzahl

print("Einzelpreis:", preis)
print("Anzahl:", anzahl)
print("Gesamtpreis:", gesamtpreis)

# Strings verketten mit +
vorname = "Max"
nachname = "Mustermann"
print("Hallo " + vorname + " " + nachname)

# Hinweis:
# Bei Zahlen addiert + die Werte
# Bei Strings verbindet + die Texte miteinander
# Geht nicht! print("5" + 10)

# ------------------------------------------------------------
# 4. round() Ergebnisse runden
# ------------------------------------------------------------

ergebnis = 10 / 3
print(ergebnis)
print(round(ergebnis))          # Auf ganze Zahl abgerundet
print(round(ergebnis, 2))       # 3.33 auf zwei Nachkommastellen gerundet

# round(wert, stellen) der zweite Parameter gibt die Nachkommastellen an

# ------------------------------------------------------------
# 5. Operatorenpräzedenz (Reihenfolge der Auswertung)
# ------------------------------------------------------------
# Python wertet Rechenoperationen nicht einfach von links nach rechts aus,
# sondern folgt festen Regeln – genauso wie in der Mathematik.
#
# Reihenfolge (von hoch nach niedrig):
#   1. Klammern ()
#   2. Potenzen **
#   3. Multiplikation *, Division /, Ganzzahl-Division //, Modulo %
#      → gleichrangig: von links nach rechts
#   4. Addition +, Subtraktion -
#      → gleichrangig: von links nach rechts

#        5
result = 3 + 4 * (7 - 5) / 2 ** 2
print(result)



