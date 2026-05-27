#Aufgabe 2: Schere, Stein, Papier

import random

erraten_zahl =random.randint(1, 100)





versuch_zahl=0

while True:

    #try:  # Hier steht der Code wo Fehler entstehen könnten
    zahl = int(input("Erraten Sie eine Zahl"))
       # if 1 <= zahl <= 100:
          #  print("Ungultige Eingabe: Zahl muss zwischen 1 und 100 liegen")

     #except ValueError as err:  # Hier steht was passiert, wenn ein Fehler ausgelöst wurde
       # print(f"Fehler: Das war keine  Zahl! {err}")



    #print(erraten_zahl)
    if erraten_zahl > zahl:
        print("Zu klein!")
        versuch_zahl=versuch_zahl + 1
        continue
    elif erraten_zahl < zahl:
        print("Zu groß!")
        versuch_zahl = versuch_zahl + 1
        continue
    elif erraten_zahl == zahl:

        break
versuch_zahl += 1
print(f"Sie haben {versuch_zahl} mal versucht. Ihre gesuchte Zahl war {erraten_zahl}")
