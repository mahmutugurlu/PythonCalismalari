# Aufgabe 1: Fehlersuche
alter = 17
punkte = 200
ist_aktiv = True
gewicht = 72.5
print("Alter in 10 Jahren:", alter + 10)
print("Doppelte Punkte:", punkte * 2)
print("Aktiv:", ist_aktiv)
print("Gewicht:", gewicht)

# Aufgabe 2: Programm umschreiben

name = "Max"
stadt_name = "Berlin"

print("Hallo", name, "!")
print("Schön, dass du dabei bist", name)
print("Unser Kurs findet in", stadt_name, "statt.")

print("Wir freuen uns auf dich in", stadt_name, name, "!")

# Aufgabe 3: Variablen tauschen

a = "Hallo"
b = "Welt"

b = (" Hallo")
a = ("Welt")
print(b, a)

# Aufgabe 4: Ticketsystem

# Verfügbare Plätze: 100
# Nach Schritt 1: 70 Plätze verfügbar
# Nach Schritt 2: 45 Plätze verfügbar
# Nach Schritt 3: 35 Plätze verfügbar
# ------------------------------
# Verkaufte Tickets: 65
# Einnahmen: 812.5 €

platz = 100
ticket_preis = 12.5
verkaufterplatz = 30 + 25 + 10
print(verkaufterplatz)  # 65
reste_platz = platz - verkaufterplatz
print(reste_platz)

print("Verkaufte Tickets:", verkaufterplatz)

print("Einnahme :", verkaufterplatz * ticket_preis)

# [Bonus] Helden-Steckbrief

spieler_name = "Lukas"
klasse = "Zauberer"
spieler_level = 6
lebenspunkte = 150
bewegungstempo = 1.25
lebendig = True

print("====== Helden-Steckbrief ======")
print("Klasse:", klasse)
print("Level:", spieler_level)
print("Lebenspunkte:", lebenspunkte)
print("Bewebungstempo:", bewegungstempo)
print("Lebendig:", lebendig)
