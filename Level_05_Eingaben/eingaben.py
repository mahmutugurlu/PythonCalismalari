# ===============================
# 1. Benutzereingaben mit input()
# ===============================
# Mit input() können wir Benutzer zur Laufzeit um Eingaben bitten
# Die Eingabe erfolgt über die Konsole
# input() gibt IMMER einen String (Text) zurück

# print("Bitte gib deinen Namen ein: ")
name = input("Bitte gib deinen Namen ein: ")
print("Hallo", name)

# ===============================
# 2. input() und Zahlen
# ===============================
# Auch wenn der Benutzer eine Zahl eingibt, ist das Ergebnis ein String

alter = input("Bitte gib dein Alter ein: ")
print("Dein Alter ist:", alter)

# Datentyp ist String
print(type(alter))

# ===============================
# 3. Datentypen umwandeln
# ===============================
# Um mit Zahlen rechnen zu können, müssen wir den String umwandeln
# Dies nennt man Casting

alter = int(alter)
print(type(alter))
alter = alter + 2
print(f"In zwei Jahren bin ich {alter} Jahre alt")

# ===============================
# 4. input() mit int()
# ===============================

zahl1 = int(input("Bitte gib eine Zahl ein: "))          # Bsp: 35
zahl2 = int(input("Bitte gib eine weitere Zahl ein: "))

summe = zahl1 + zahl2
print(f"Die Summe von {zahl1} + {zahl2} beträgt {summe}")

# ===============================
# 4. input() mit float()
# ===============================

preis = float(input("Bitte gib einen Preis ein: "))
menge = float(input("Bitte gib eine Menge ein: "))

gesamtpreis = preis * menge
print(f"Der Gesamtpreis beträgt {gesamtpreis}")

# ===============================
# 5. Casting zurück zu String
# ===============================
# Manchmal möchten wir auch wieder Zahlen in Strings umwandeln
punkte = 65
print("Erreichte Punktzahl: " + str(65))