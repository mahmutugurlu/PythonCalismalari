print(" "," ","*")
print(" ","*","*","*")
print("*","*","*","*","*")
print(" ","*","*","*")
print(" "," ","*")

#Kommentare erklären den Code für Menschen. Python ignoriert sie vollständig. Wichtig zum Strukturieren und Dokumentieren von Programmen.

# Python ignoriert diese Zeile
x = 5  # Kommentar am Zeilenende

print("-"*10)

#Gibt Werte auf dem Bildschirm aus. Mehrere Werte werden mit Komma getrennt. Python fügt automatisch ein Leerzeichen dazwischen ein.

print("Text")       # String
print(42)           # Zahl
print(10 + 5)      # Ausdruck
print("x =", 42)   # mehrere Werte

print("-"*10)

#sep= und end=
#Mit sep= das Trennzeichen zwischen Werten anpassen, mit end= den automatischen Zeilenumbruch ersetzen.

print("a", "b", "c", sep="-")#sep Python’da print() fonksiyonunun bir parametresidir ve çıktıda yazılan değerlerin arasına ne konulacağını belirler.
# a-b-c                      #Der sep-Parameter definiert das Trennzeichen zwischen mehreren Ausgaben im print()-Befehl.

print("Teil 1", end=" | ")
print("Teil 2")
# Teil 1 | Teil 2

print("-"*10)

#Escape-Sequenzen
#Sonderzeichen, die nicht direkt in einen String geschrieben werden können, werden mit einem vorangestellten \ eingeleitet.

#Sequenz	Bedeutung
#\n	Zeilenumbruch
#\t	Tabulator   --\t = imleci sağa atlatır (kolon hizalar) -- \t = bewegt den Cursor nach rechts (richtet Spalten aus)
#\\	Backslash \
#\"	Doppeltes Anf.-zeichen
#\'	Einfaches Anf.-zeichen
print("Zeile 1\nZeile 2")
print("Pfad: C:\\Users\\Name")

print("-"*10)

#Strings verbinden & wiederholen
#Mit + zusammensetzen, mit * vervielfältigen. Beide Operatoren funktionieren nur zwischen gleichen Typen.

"Hallo" + " Welt"
# "Hallo Welt"

"-" * 20
# "--------------------"