#Aufgabe 1: Sich selbst vorstellen mit f-String

name = "Mahmut"
alter = 37
lieblingsessen = "Türkische Küche"

print(f"Hi! Mein Name ist {name}. Ich bin {alter} Jahre alt und mein Lieblingsessen ist {lieblingsessen}.")


print("-"*20)


#Aufgabe 2: Verkaufszahlen formatiert ausgeben

umsatzsteigerung_prozent = 12.93720081
umsatzwachstum_prozent = 18.33206078

print(f"Unser Umsatz stieg um {umsatzsteigerung_prozent:.2f}% und unser Gesamtumsatz wuchs um {umsatzwachstum_prozent:.2f} %."
)



print("-"*20)




#Aufgabe 3: Tabelle mit Name, Alter und Kosten ausgeben

#Name Alter Betrag
#---------------------------------
#Alice 28 45.00 €
#Bob 34 1200.50 €
#Clara 19 7.99 €

name1 = "Alice"
name2 = "Bob"
name3 = "Clara"

alter1 = 28
alter2 = 34
alter3 = 19

betrag1 = 45.00
betrag2 = 1200.50
betrag3 = 7.99

print(f"{"Name":<10}{"Alter":^18}{"Betrag":>8} ")

print("-"*40)

print(f"{name1:<15} {alter1:>3}  {betrag1:>14.2f}€" )
print(f"{name2:<15} {alter2:>3}  {betrag2:>14.2f}€" )
print(f"{name3:<15} {alter3:>3}  {betrag3:>14.2f}€" )



print("-"*20)

#Aufgabe 1: Kassenbon


laden = "Frischemarkt Müller"
artikel1 = "Milch"
menge1 = 2
preis1 = 1.09*menge1
artikel2 = "Brot"
menge2 = 1
preis2 = 2.49*menge2
artikel3 = "Käse"
menge3 = 3
preis3 = 0.89*menge3
rabatt = 0.10 # 10% Rabatt

zwischensumme=preis2+preis3+preis1
rabatt_gebühr= 0.10*zwischensumme # bir variablayi kullanmak icin kullanmak istedigin yerden önce yaz
gesamt_preis = zwischensumme-rabatt_gebühr

print("=" * 24)

print(f"{laden:^24} ")

print("=" * 24)

print(f"{"Artikel":<10}{"Anz.":^18}{"Preis":>8} ")

print("-"*20)


print(f"{artikel1:<15} {menge1:>3}  {preis1:>14.2f}€" )
print(f"{artikel2:<15} {menge2:>3}  {preis2:>14.2f}€" )
print(f"{artikel3:<15} {menge3:>3}  {preis3:>14.2f}€" )
print("-"*20)

print(f"{"Zwischensumme:":<15}   {zwischensumme:>17.2f}€" )
print(f"{"Rabatt (10%): ":<15}   {rabatt_gebühr:>17.2f}€" )

print("-"*20)

print(f"{"GESAMT: ":<15}   {gesamt_preis:>17.2f}€" )

print("=" * 24)
