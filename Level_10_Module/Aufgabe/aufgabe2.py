#Aufgabe 2: Schere, Stein, Papier

import random
from queue import PriorityQueue

spiel_list=["Schere", "Stein", "Papier"]
computer_auswahl=random.choice(spiel_list)

schere="Schere"
stein="Stein"
papier="Papier"
quit="quit"



spiel_zahl=0
niederlagen_zahl=0
unentschieden_zahl=0
gewinnt_zahl=0


while True:
    spiel_list = ["Schere", "Stein", "Papier"]
    computer_auswahl = random.choice(spiel_list)
    print(computer_auswahl)
    benutzer_auswahl = input("Schreiben  Sie Ihr Auswahl")

    if benutzer_auswahl == computer_auswahl:
        print("Unentschieden!")
        spiel_zahl=spiel_zahl+1
        unentschieden_zahl = unentschieden_zahl + 1
        continue

    elif benutzer_auswahl == schere and computer_auswahl == papier:
        print("Du gewinnst!")
        spiel_zahl=spiel_zahl+1
        gewinnt_zahl = gewinnt_zahl + 1
        continue

    elif benutzer_auswahl == schere and computer_auswahl == stein:
        print("Verloren!")
        spiel_zahl=spiel_zahl+1
        niederlagen_zahl = niederlagen_zahl + 1
        continue

    #if benutzer_auswahl == computer_auswahl:
     #   print("Unentschieden!")
      #  spiel_zahl = spiel_zahl + 1
       # unentschieden_zahl = unentschieden_zahl + 1
        #continue

    elif benutzer_auswahl == stein and computer_auswahl == schere:
        print("Du gewinnst!")
        spiel_zahl = spiel_zahl + 1
        gewinnt_zahl = gewinnt_zahl + 1
        continue

    elif benutzer_auswahl == stein and computer_auswahl == papier:
        print("Verloren!")
        spiel_zahl = spiel_zahl + 1
        niederlagen_zahl = niederlagen_zahl + 1
        continue


    elif benutzer_auswahl == papier and computer_auswahl == stein:
        print("Du gewinnst!")
        spiel_zahl = spiel_zahl + 1
        gewinnt_zahl = gewinnt_zahl + 1
        continue

    elif benutzer_auswahl == papier and computer_auswahl == schere:
        print("Verloren!")
        spiel_zahl = spiel_zahl + 1
        niederlagen_zahl = niederlagen_zahl + 1
        continue

    elif benutzer_auswahl == quit:
        break


print("Spiele: ",spiel_zahl)
print("Niederlagen: ",niederlagen_zahl)
print("Unentschieden: ",unentschieden_zahl)
print("Siege: ", gewinnt_zahl)


