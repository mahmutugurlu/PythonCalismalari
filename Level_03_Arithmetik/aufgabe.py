#Aufgabe 1: Rechteck berechnen
heohe=10
breit = 15
umfang = 2*(heohe+breit)
print(umfang) #50
fläche = heohe*breit
print(fläche) #150


print("-"*20)


#Aufgabe 2: Operatorenpräzedenz

print( 2 + 3 * 4) #14 +
print( (2 + 3) * 4) #20 +
print(10 - 4 / 2 ) #8 +
print((10 - 4) / 2) #3 +
print( 5 + 8 * (9 - 5) / 2 ** 4) #7+


print("-"*20)



#Aufgabe 3: Minuten in Stunden umrechnen

werte = 156
uhrzeit= 60
uhr = werte//uhrzeit,
minuten= werte%uhrzeit

print(uhr,"Stunden ", "und ", minuten,"Minuten")


print("-"*20)


#Aufgabe 4: Rabatt und Steuern

erste_preis =120
rabattanteil=15
rabattanteil_anwendung=rabattanteil/100
steuerantei = 19/100

rabattpreis= erste_preis- erste_preis*rabattanteil_anwendung
print("Preis nach Rabatt:",rabattpreis)

verkauftpreis= rabattpreis + rabattpreis*steuerantei
print("Endpreis inkl. Mehrwertsteuer:",verkauftpreis)






print("-"*20)


#[Bonus] Quersumme einer Zahl

zahl: 1453
ziffer1=1
ziffer2= 4
ziffer3=5
ziffer4= 3
quersumme=(ziffer1+ziffer2+ziffer3+ziffer4)
print(quersumme)




# ============================================================
# Aufgabe: Quersumme einer Zahl – Beispiellösung
# ============================================================

zahl = 2748

# ------------------------------------------------------------
# Schritt 1: Ziffern einzeln herausrechnen
# ------------------------------------------------------------
# Die Grundidee:
#   zahl % 10   → liefert immer die letzte Ziffer
#   zahl // 10  → schneidet die letzte Ziffer ab
#
# Diesen Vorgang wiederholt man von rechts nach links.

# Ziffer 4 (letzte Stelle: 8)
ziffer_4 = zahl % 10           # 2748 % 10 = 8
zahl = zahl // 10              # 2748 // 10 = 274

# Ziffer 3 (neue letzte Stelle: 4)
ziffer_3 = zahl % 10           # 274 % 10 = 4
zahl = zahl // 10              # 274 // 10 = 27

# Ziffer 2 (neue letzte Stelle: 7)
ziffer_2 = zahl % 10           # 27 % 10 = 7
zahl = zahl // 10              # 27 // 10 = 2

# Ziffer 1 (verbleibende Stelle: 2)
ziffer_1 = zahl % 10           # 2 % 10 = 2

# ------------------------------------------------------------
# Schritt 2: Quersumme berechnen
# ------------------------------------------------------------

quersumme = ziffer_1 + ziffer_2 + ziffer_3 + ziffer_4

# ------------------------------------------------------------
# Schritt 3: Ausgabe
# ------------------------------------------------------------

print("Zahl: 2748")
print("Ziffer 1:", ziffer_1)
print("Ziffer 2:", ziffer_2)
print("Ziffer 3:", ziffer_3)
print("Ziffer 4:", ziffer_4)
print("Quersumme:", quersumme)