# ============================================================
# EINHEIT 08: Listen
# ============================================================

# ------------------------------------------------------------
# THEORIE: Was sind Listen und warum brauchen wir sie?
# ------------------------------------------------------------
# Bisher haben wir für jeden Wert eine eigene Variable gebraucht:
#   artikel1 = "Milch"
#   artikel2 = "Brot"
#   artikel3 = "Butter"
#
# Das wird schnell unpraktisch, wenn wir viele Artikel speichern wollen.
# Eine Liste löst das: Sie ist ein Behälter, der beliebig viele Werte speichert.
#
# Listen sind:
#   - geordnet     → die aktuelle Reihenfolge bleibt erhalten
#   - veränderlich → Elemente können hinzugefügt, entfernt und ersetzt werden
#   - gemischt     → verschiedene Datentypen möglich, in der Praxis meist gleicher Typ

# ------------------------------------------------------------
# BEISPIEL 1: Liste erstellen
# ------------------------------------------------------------
# Wir legen unsere Einkaufsliste an und arbeiten im Folgenden mit ihr.
# Listen können leer erstellt oder direkt mit Werten befüllt werden.

# Leere Liste:
leere_liste = []

# Liste mit Startwerten
zahlen_liste = [1, 5, 22, 3, 14, 35]
gemischte_liste = ["Hello", 3.14, 42, True, "Käse"]

# dictionary Beispiel
dictionary = {"Nico Geromin": 1234}

# Unsere Einkaufsliste für diese Einheit:
einkaufsliste = ["Milch", "Eier", "Butter", "Brot", "Kartoffeln", "Pferdesalami", "Tofu", "Kreuzkümmel"]

print(einkaufsliste)
print(len(einkaufsliste))            # len() gibt die Anzahl der Elemente zurück

# ------------------------------------------------------------
# BEISPIEL 2: Indexierung – auf einzelne Elemente zugreifen
# ------------------------------------------------------------
# Jedes Element hat eine Position (Index), beginnend bei 0.
# Negative Indizes zählen vom Ende der Liste:
#   -1 = letztes Element, -2 = vorletztes usw.

#  Elemente          [1]     [2]      [3]       [4]        [5]            [6]         [7]        [8]
#  Index             [0]     [1]      [2]       [3]        [4]            [5]         [6]        [7]
# einkaufsliste = ["Milch", "Eier", "Butter", "Brot", "Kartoffeln", "Pferdesalami", "Tofu", "Kreuzkümmel"]
# negativer Index    [-8]     [-7]      [-6]       [-5]     [-4]        [-3]         [-2]        [-1]

print(einkaufsliste[0])
print(einkaufsliste[2])
print(einkaufsliste[-1])

# index() Index des ersten Vorkommens eines Wertes ermitteln
print(einkaufsliste.index("Tofu"))

# ------------------------------------------------------------
# BEISPIEL 3: Elemente hinzufügen und ersetzen
# ------------------------------------------------------------

# append() Element ans Ende anhängen
einkaufsliste.append("Mehl")
print(einkaufsliste)

# insert() Element an bestimmter Position einfügen
# insert(index, wert) fügt dem Wert VOR dem Element an diesem Index ein
einkaufsliste.insert(1, "Joghurt")
print(einkaufsliste)

# Element ersetzen
einkaufsliste[0] = "Vollmilch"
print(einkaufsliste)

# ------------------------------------------------------------
# BEISPIEL 4: Elemente entfernen
# ------------------------------------------------------------

# remove() erstes Vorkommen eines bestimmten Wertes entfernen
einkaufsliste.remove("Joghurt")
print(einkaufsliste)

# del - Element an bestimmten Index löschen
del einkaufsliste[2]
print(einkaufsliste)

# pop() letztes Element entfernen (und zurückgeben)
letztes_element = einkaufsliste.pop(einkaufsliste.index("Eier"))
# letztes_element = einkaufsliste.pop(-2)
print(letztes_element)
print(einkaufsliste)

# Funktion ohne Parameter, entfernt alle Elemente aus einer Liste
# einkaufsliste.clear()
# print(einkaufsliste)

# ------------------------------------------------------------
# BEISPIEL 5: Weitere nützliche Funktionen für Listen
# ------------------------------------------------------------

# in-Operator, ist ein Wert in einer Liste enthalten?
print("Brot" in einkaufsliste)
print("Zucker" in einkaufsliste)

# count() Wie oft kommt ein Wert in einer Liste vor?
einkaufsliste.append("Tofu")
print(einkaufsliste.count("Tofu"))

# sort() Liste aufsteigend sortieren (verändert die Liste direkt)
einkaufsliste.sort()
print(einkaufsliste)

# absteigende Sortierung
einkaufsliste.sort(reverse=True)
print(einkaufsliste)

# reverse() Liste umkehren
einkaufsliste.reverse()
print(einkaufsliste)

# gemischte_liste.sort()
# print(gemischte_liste)

# kopierte_liste = einkaufsliste
# print(einkaufsliste)
# print(kopierte_liste)
# kopierte_liste.sort(reverse=True)
# print("Nach Sortierung:", einkaufsliste)
# print("Nach Sortierung:", kopierte_liste)

# kopie = list(einkaufsliste)
# kopie.sort(reverse=True)
# print("Nach Sortierung:", einkaufsliste)
# print("Nach Sortierung:", kopie)

kopie = einkaufsliste.copy()
kopie.sort(reverse=True)
print("Nach Sortierung:", einkaufsliste)
print("Nach Sortierung:", kopie)

# ------------------------------------------------------------
# BEISPIEL 6: Mit for über eine Liste iterieren
# ------------------------------------------------------------
# Die for-Schleife kennen wir aus Level 07 mit range()
# Sie funktioniert genauso mit Listen.
# Python geht dabei automatisch von Element zu Element, ohne dass wir einen Index brauchen

# print("Einkaufsliste: ")
# for artikel in einkaufsliste:
#     print(artikel)

print("Artikel mit mehr als 4 Buchstaben")
for artikel in einkaufsliste:
    if len(artikel) > 4:                        # Strings sind auch Listen ['T', 'o', 'f', 'u']
        print(f"    - {artikel}")