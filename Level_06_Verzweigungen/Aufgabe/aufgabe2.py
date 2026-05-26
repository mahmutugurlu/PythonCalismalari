#Aufgabe 2: Einfacher Login
eingabe_benutzername= input("Bitte geben Sie Ihre Benutzername")
eingabe_passwort= input("Bitte geben Sie Ihr Passwort")

benutzername= "Admin"
passwort= "geheim123"

if benutzername==eingabe_benutzername and passwort == eingabe_passwort:
    print("Willkommen, admin! Du bist eingeloggt.")
else:
    print("Benutzername oder Passwort falsch.")