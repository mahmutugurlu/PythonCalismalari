#Aufgabe 1: Notenverwaltung
from Level_03_Arithmetik.aritmetik import anzahl
noten_list = []
summe = 0

while True:
    eingabe = input("Note eingeben (Enter zum Beenden): ")

    if eingabe == "":
        break

    note = int(eingabe)
    noten_list.append(note)

print("Noten:", noten_list)

anzahl = len(noten_list)

if anzahl > 0:
    durch = sum(noten_list) / anzahl
    print("Durchschnitt:", f"{durch:.2f}")

    beste = min(noten_list)
    print("Beste Note:", beste)

    schlechteste = max(noten_list)
    print("Schlechteste Note:", schlechteste)
else:
    print("Keine Noten eingegeben.")






