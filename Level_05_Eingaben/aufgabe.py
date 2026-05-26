#Aufgabe 1: Bandnamen-Generator

stadt_name = input("Willkommen beim Bandnamen-Generator! In welcher Stadt bist du aufgewachsen?")
print(stadt_name)
tier_name = input("Wie lautet dein Lieblingstier in Englisch?")
print(tier_name)

bandnamer= stadt_name+"er "+ tier_name+"s"
print("Dein möglicher Bandname ist:", bandnamer )


print("-"*30)

#######################################################################

#Aufgabe 2: Warenkorb
artikel = input("Welchen Artikel möchtest du kaufen?")
preis_artikel= float(input("Was kostet der Artikel?"))
menge_artikel= int(input("Wie viele Stück möchtest du kaufen?"))

gesamt_preis = preis_artikel*menge_artikel

print(f"Du hast {menge_artikel} Pizza gekauft")
print(f"Der Gesamtpreis ist {gesamt_preis} €")

#######################################################################


print("-"*30)


##################################################

#Aufgabe 3: Einheiten-Umrechner


zahl= int(input("Bitte gib eine Zahl ein:"))

ein_km=zahl
ein_meil= ein_km*0.621
print(f"100 Kilometer sind {ein_meil} Meilen")


ein_meil=zahl
ein_km= ein_meil*1.609
print(f"100 Meilen sind {ein_km} Meilen")

zentimeter=zahl
inch = zentimeter*0.394
print(f"100 Zentimeter sind {inch} Inches.")

inch=zahl
zentimeter= inch*2.54
print(f"100 Inches sind {zentimeter} Zentimeter.")



euro=zahl
pfund= euro*0.8547
print(f"100 Euro sind {pfund} Pfund.")


pfund=zahl
euro= pfund*1.17
print(f"100 Pfund sind {euro} Euro.")