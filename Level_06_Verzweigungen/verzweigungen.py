# ========================================
# 1. Vergleichsoperatoren
# ========================================
# Vergleichsoperatoren prüfen und vergleichen Werte und ergeben einen boolschen Ausdruck - True und False

a = 5
b = 3

print(a == b)       # genau gleich -> False
print(a != b)       # nicht gleich/ungleich -> True
print(a < b)        # kleiner als -> False
print(a <= b)       # kleiner oder gleich -> False
print(a > b)        # größer als -> True
print(a >= b)       # größer oder gleich -> True

# ========================================
# 2. Einfache if-Bedingung
# ========================================
# Mit "if" können wir entscheiden, ob ein bestimmter Codeblock ausgeführt wird
# Die Bedingung muss einen Wahrheitswert (True oder False) liefern

alter = int(input("Bitte geben Sie Ihr Alter ein: "))

# Syntax: if [Bedingungsprüfung die True oder False ergibt]
# if alter >= 18:
#     print("Du bist volljährig")

# if alter >= 18:                    # Prüfung: ist alter größer oder gleich 18?
#      print("Du bist volljährig")   # Dieser Code wird nur ausgeführt, wenn alter >= 18 True ergibt

# ========================================
# 3. if-else
# ========================================
# Mit if-else können wir zwei alternative Aktionen ausführen
# wenn die Bedingung True ergibt, wird der if-Block ausgeführt
# ansonsten wird der else Block ausgeführt

# if alter >= 18:
#     print("Du bist volljährig")
# else:
#     print("Du bist noch minderjährig")

# ========================================
# 4. if-elif-else
# ========================================
# Mit if-elif-else können wir mehrere Bedingungen nacheinander prüfen
# Nur der erste Block der True ergibt wird ausgeführt

if alter >= 65:
    print("Seniorenrabatt: 30% Ermäßigung")
elif alter >= 18:
    print("Regulärer Eintrittspreis")
elif alter >= 6:
    print("Kinderrabatt: 50% Ermäßigung")
else:
    print("Kinder unter 6 Jahren: Eintritt frei")

# Debugger Test
zahl = 5
zahl += 10
zahl = zahl + zahl
print()

# ========================================
# 5. Logische Operatoren
# ========================================
# Logische Operatoren erlauben das Verknüpfen von Bedingungen
# Dabei kann jeder Ausdruck verwendet werden, der einen Wahrheitswert ergibt
# z.B Vergleiche "alter >= 18", boolsche Variablen und Funktionsaufrufe

# and -> beide Bedingungen müssen True sein
# or  -> mindestens eine Bedingung True sein muss
# not -> kehrt einen Wahrheitswert um

hat_ticket = False
ist_auf_liste = False

# AND Verknüpfung
# if hat_ticket and ist_auf_liste:
#     print("Willkommen! Du kommst rein")
# else:
#     print("Kein Einlass - beide Bedingungen müssen erfüllt sein")

# OR Verknüpfung
# if hat_ticket or ist_auf_liste:
#     print("Willkommen! Du kommst rein")
# else:
#     print("Weder Ticket noch auf der Liste - kein Einlass")

# NOT - Bedingung umkehren
# if not hat_ticket:
#     print("Du hast ein Ticket")

if alter >= 18 and alter <= 65:
    print("Du bist berufstätig")
else:
    print("Schön, dass du soviel Freizeit hast")

hat_fuehrerschein = True

#     False             True
if alter >= 18 or hat_fuehrerschein:
    print("Viel Spaß beim Autofahren")

#   True
if not alter >= 18:
    print("Du bist noch ein Kind")

# ========================================
# 6. Verschachtelte if-Bedingungen
# ========================================
# if-Bedingungen können innerhalb anderer if-Bedingungen stehen

kontostand = 250
betrag = 200
konto_gesperrt = False

if konto_gesperrt:
    print("Transaktion nicht möglich: Konto ist gesperrt")
else:
    if kontostand >= betrag:
        print("Transaktion erfolgreich")
    else:
        print("Transaktion nicht möglich: Kontostand ist zu niedrig")

# Hinweis: Verschachtelungen können beliebig tief sein, aber zu tiefe Verschachtelungen werden unübersichtlich

# ========================================
# 7. match-case (Python 3.10)
# ========================================
# Alternative zu langen if-elif Ketten
# Gut geeignet, wenn ein Wert gegen feste Option geprüft wird
# Nur der erste passende case wird ausgeführt


print("\n--- Bestellsystem ---")
status = input("Bestellstatus eingeben (neu/verarbeitung/versandt/storniert): ")
match status:
    case "neu":
        print("Bestellung eingegangen - wird geprüft")
    case "verarbeitung":
        print("Bestellung wird aktuell bearbeitet")
    case "versandt":
        print("Bestellung ist unterwegs")
    case "storniert":
        print("Bestellung wurde storniert")
    case _:     # _ ist der Default-Case, greift wenn kein anderer case passt (wie else)
        print(f"Unbekannter Bestellstatus: '{status}'")

