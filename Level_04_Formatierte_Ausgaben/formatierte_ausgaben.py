# ============================================
# 1- Formatierte Ausgaben mit f-Strings
# ============================================
# f-Strings erlauben es, Variablen direkt in einen String einzubetten
# Dazu wird vor den String ein f geschrieben
# Variablen werden in geschweifte Klammern {} gesetzt

name = "Maximilian"
alter = 33

# Ohne f-String
print("Mein Name ist", name)
# Mit f-String
print(f"Mein Name ist {name}")

# Auch Rechenausdrücke möglich
print(f"In zwei Jahren bin ich {alter + 2} Jahre alt")

# f-Strings als Variable speichern
begruessung = f"Hallo, mein Name ist {name} und ich bin {alter} Jahre alt."
print(begruessung)

# ============================================
# 2. Zahlen formatieren (Nachkommastellen)
# ============================================
# Mit :.<anzahl>f können Nachkommastellen begrenzt werden

kontostand = 1234.56789
print(f"Aktueller Kontostand: {kontostand:.2f} Euro")
print(f"Aktueller Kontostand: {kontostand:.3f} Euro")

# ============================================
# 3. Formatierte Ausgaben mit format()
# ============================================
# Die format()-Methode ist eine ältere, aber weiterhin gültige Methode
# Platzhalter {} werden der Reihenfolge nach gefüllt

print("Mein Name ist {} und ich bin {} Jahre alt.".format(name, alter))

# Platzhalter können nummeriert werden
print("Name: {1}, Alter: {0}".format(alter, name))

# ============================================
# 4. Feldbreite und Ausrichtung
# ============================================
# Mit :N (wobei N eine Zahl ist) reservieren wir N Zeichen Feldbreite
# Das ermöglicht uns saubere Tabellenausrichtung
#   :>N     rechtsbündig
#   :<N     linksbündig
#   :^N     zentriert

# Ausgabe:
# ========================
#       Frischemarkt
# ========================
# Produkt            Preis
# ------------------------
# Apfel               1.29
# Wassermelone        3.99

print("=" * 24)
print(f"{"Frischemarkt":^24}")
print("=" * 24)

# Linksbündig / Rechtsbündig für Tabellenspalten
print(f"{"Produkt":<12}{"Preis":>12}")
print("-" * 24)
print(f"{"Apfel":<5}{"1.29":>19}")
print(f"{"Wassermelone":<12}{"3.99":>12}")

ueberschrift = "Frischemarkt"
spaltenueberschrift1 = "Produkt"
spaltenueberschrift2 = "Preis"

artikel1 = "Apfel"
artikel2 = "Wassermelone"

preis1 = 1.29
preis2 = 3.99

print("=" * 24)
print(f"{ueberschrift:^24}")
print("=" * 24)

# Linksbündig / Rechtsbündig für Tabellenspalten
print(f"{spaltenueberschrift1:<12}{spaltenueberschrift2:>12}")
print("-" * 24)
print(f"{artikel1:<12}{preis1:>12}")
print(f"{artikel2:<12}{preis2:>12}")