# ==============================================================================
# THEORIE: Was ist Python und was ist ein Programm?
# ==============================================================================
#
# Ein Programm ist eine Abfolge von Anweisungen, die der Computer
# von oben nach unten ausführt (wie ein Rezept).
#
# Python liest jede Zeile und führt sie sofort aus.
# Zeilen mit # sind Kommentare. Python ignoriert sie.
# Sie dienen uns zur Strukturierung und Erklärung des Codes.
#
# Die allererste Fähigkeit: Dem Computer sagen, er soll etwas auf dem Bildschirm ausgeben.
# Dazu stellt Python die sogenannte print() Funktion bereit.
#
# ==============================================================================

# Mit Strg + / (Numpad) Kommentarblock ein oder auskommentieren
# Hallo hier steht Text
# hier gehts weiter
# usw.

# -----------------------------
# 1. Text und Zahlen ausgeben
# -----------------------------
# Text (sog. "Strings") wird in Anführungszeichen geschrieben
# Einfache oder doppelte Anführungszeichen sind beide erlaubt

print("My name is Jeff")
print('Jeff mit einfachen Anführungszeichen')

# Zahlen brauchen keine Anführungszeichen, Python kann mit ihnen rechnen
print("42")     # 42 als Text
print(42)       # 42 als Zahl
print(2.54)     # Kommazahl: Punkt statt Komma!
print(10 + 5)
print(10 * 5)

print()

# -----------------------------
# 2. Mehrere Werte in einem print() Befehl nutzen
# -----------------------------
# print() kann mehrere Werte auf einmal ausgeben. Sie werden durch ein Komma getrennt
# Python fügt automatisch ein Leerzeichen zwischen den Werten ein

print("Mein Name ist", "Maximlian")
print("Ich bin", 33, "Jahre alt")
print("Das Ergebnis ist:", 10 + 3)

print("Hallo ich bin ein sehr langer Text",
      "irgendwann fliege ich aus dem Bildschirm")

print()

# -----------------------------
# 3. Escape-Sequenzen und Steuerzeichen
# -----------------------------
print("Er sagte: 'Hallo'")
print('Er sagte: "Hallo"')

print("Zitat: \"Python ist toll\"")     # \"    Durch das Backslash wird das folgende Anführungszeichen mit ausgegeben
print("Erste Zeile\nZweite Zeile")      # \n    (newline) erzeugt Zeilenumbruch
print("Spalte1\tSpalte2\tSpalte3")      # \t erzeugt Einrückung

print("Pfad: C:\\Users\\Azubi")
print(r"Pfad: C:\Users\Azubi")

# -----------------------------
# 4. sep= zum Anpassen des Trennzeichens
# -----------------------------
# Standardmäßig trennt print() mehrere Werte mit einem Leerzeichen
# Mit sep= (separator = Trennzeichen) können wir das ändern

print("2026", "05", "19", sep="-")
print("Apfel", "Banane", "Kirsche", sep=", ")

print()

# -----------------------------
# 5. Das end-Argument -> Zeilenende anpassen
# -----------------------------
# print() macht nach jeder Ausgabe einen Zeilenumbruch
# Mit end= können wir festlegen, was stattdessen am Ende steht

print("Ich bin ", end="")
print("in einer Zeile")

print("Zeile 1", end=" | ")         # Trennzeichen statt Zeilenumbruch
print("Zeile 2", end=" | ")
print("Zeile 3")

# -----------------------------
# 6. Strings verbinden und wiederholen
# -----------------------------
# Strings können mit einem + verbunden (konkateniert) werden

print("My name is " + "Jeff")
# print("3" + 5)        # Text und Zahlen können nicht mit + verkettet werden

# Strings können mit * wiederholt werden
print("----------")
print("-" * 10)