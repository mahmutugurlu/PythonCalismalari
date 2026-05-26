# ==========================================
# 1. Was sind Schleifen?
# ==========================================
# Schleifen erlauben es, Code mehrfach auszuführen,
# ohne ihn immer wieder neu schreiben zu müssen.
#
# In Python gibt es zwei wichtige Schleifen:
# - for-Schleife  -> Zählschleife
# - while-Schleife -> Bedingungsschleife


# ==========================================
# 2. Die for-Schleife (Zählschleife)
# ==========================================
# Die for-Schleife wird verwendet, wenn die Anzahl
# der Wiederholungen bereits bekannt ist
# range(start, stop, step) erzeugt eine Zahlenfolge.

# for-Schleife mit Endwert      [0, 1, 2, 3, 4]
for zahl in range(5):           # range(5) erzeugt die Zahlen 0 bis 4 (5 ist exklusiv)
    print("Durchlauf:", zahl)

print()

# for-Schleife mit Start- und Endwert   [3, 4, 5]
for i in range(3, 6):            # range (3, 6) erzeugt die Zahlen 3 bis 5
    print("Durchlauf:", i)

print()

# for-Schleife mit Schrittweite   [0, 2, 4, 6, 8, 10]
for wert in range(0, 11, 2):    # Schrittweite von 2, jeden Schleifendurchluaf wird der Zähler um 2 erhöht
    print("Gerade Zahlen", wert)

# Rückwärts zählen                [100, 99, 98, 97 ... 21]
for rueck in range(100, 20, -1):
    print("Runterzählen:", rueck)

print()

# Beispiel mit einer Bedingungsprüfung

for zahl in range(1, 11): # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    if zahl % 2 == 0:
        print(zahl, " ist gerade")
    else:
        print(zahl, " ist ungerade")

# ==========================================
# 2. Die while-Schleife
# ==========================================
# Die while Schleife wird solange ausgeführt, wie ihre Bedingung True ist
# Sie wird verwendet, wenn die Anzahl der Durchläufe vorher nicht bekannt ist

loesungswort = ""   # Leerer String
while loesungswort != "python":         # ungleich
    loesungswort = input("Lösungswort: ")

print("Richtig geraten")

# ==========================================
# 2. break und continue
# ==========================================
# break -> Schleife sofort verlassen
# continue -> diesen Durchlauf überspringen
# while True: (Endlosschleife) läuft bis break ausgeführt wird

versuche = 0
while True:
    pin = input("PIN: ")
    versuche += 1
    if pin == "1234":
        print(f"Zugang gewährt nach {versuche} Versuche(en)")
        break               # Notausgang
    if versuche >= 3:
        print("Konto gesperrt")
        break               # Notausgang

# continue überspringt einen Durchlauf
for i in range(1, 11):
    if i % 3 == 0:
        continue
    print("Nur Zahlen die nicht durch 3 teilbar sind: ", i)