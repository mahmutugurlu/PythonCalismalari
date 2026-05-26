
#Aufgabe 1: Datentypen vorhersagen

a = 100   # int +
print(type(a))

b = 100.0  # float +
print(type(b))

c = "100" #String +
print(type(c))

d = True #bool +
print(type(d))

e = "True" #string +
print(type(e))

f = 0  #int +
print(type(f))

g = ""  #string +
print(type(g))

h = 1.0 #float +
print(type(h))



print("-"*20)



# Aufgabe 2: Ausgabe vorhersagen

x = 10
print(x) # 10 +
x = 25
print(x) #25 +
x = x + 5
print(x)  #30 +
x += 10
print(x)  #40 +
x *= 2
print(x)  #80 +



print("-"*20)



#Aufgabe 3: Was speichert b?

a = "Python"
b = a
a = "Java"
print(a) #Java
print(b) #Python


print("-"*20)

#Aufgabe 4: Variablennamen beurteilen

#2name = "Anna"    Muss mit einem Buchstaben oder _ beginnen
#mein name = "Anna"    Variablenname darf nicht getrennt geschrieben werden.
#if = 5   #   ‚if‘ darf nicht als Variablenname benutzt werden, denn es ist ein Schlüsselwort.
_geheim = True  #kein Problem
#punkte-gesamt = 10   Muss _ ( Unterstrich) sein
MeinAlter = 17   #Üblicherweise wird in Python die Schreibweise ‚snake_case‘ benutzt, trotzdem kann der Code laufen.
lieblingsfarbe = "Blau"  # Üblicherweise wird in Python die Schreibweise ‚snake_case‘ benutzt, trotzdem kann der Code laufen.

print(MeinAlter, lieblingsfarbe)


print("-"*20)


spieler_name = "Lukas"
spieler_level = 7
punkte = 1500
eingeloggt_stand = True
ping = 45.7

print("====== Helden-Steckbrief ======")
print("Name:", spieler_name)
print("Level:", spieler_level)
print("Punkte:", punkte)
print("Eingeloggt:", eingeloggt_stand)
print("Ping:", ping)
