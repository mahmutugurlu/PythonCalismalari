#Aufgabe 3: Notenrechner

punkte= int(input("Bitte gib deine Punktzahl ein:"))

if punkte>=90:
    print(f"Ergebnis: Sehr gut {punkte}")

elif punkte>=75 and punkte<=89:
    print(f"Ergebnis: Gut {punkte}")

elif 60 <= punkte <= 74:
    print(f"Ergebnis: Befriedigend {punkte}")

elif punkte>=45 and punkte<=59:
    print(f"Ergebnis: Ausreichend {punkte}")

elif punkte>=0 and punkte<=44:
    print(f"Ergebnis: Nicht bestanden {punkte}")