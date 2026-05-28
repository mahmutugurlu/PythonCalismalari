#Aufgabe 1: Bankautomat


# ===== Fonksiyonlar =====

def show_balance(balance):
    print("\nHier ist Ihr aktueller Kontostand:")
    print("##########")
    print(f"# {balance:.2f} € #")
    print("##########")


def deposit():
    while True:
        try:
            einzahlung = float(input("Wie viel möchten Sie einzahlen?: "))
            if einzahlung <= 0:
                print("Betrag muss positiv sein!")
            else:
                return einzahlung
        except ValueError:
            print("Bitte geben Sie eine gültige Zahl ein!")


def withdraw(balance):
    while True:
        try:
            amount = float(input("Wie viel möchten Sie auszahlen?: "))
            if amount <= 0:
                print("Betrag muss positiv sein!")
            elif amount > balance:
                print("Nicht genug Guthaben!")
            else:
                return amount
        except ValueError:
            print("Bitte geben Sie eine gültige Zahl ein!")


# ===== Hauptprogramm =====

balance = 100000.0

while True:
    print("\n##########")
    print("# BANK AUTOMAT #")
    print("##########")
    print("1. Kontostand anzeigen")
    print("2. Einzahlung")
    print("3. Auszahlung")
    print("4. Beenden")

    aussucht = input("Was möchten Sie tun?: ")

    if aussucht == "1":
        show_balance(balance)

    elif aussucht == "2":
        einzahlung = deposit()
        balance += einzahlung
        print(f"{einzahlung:.2f} € wurden eingezahlt.")

    elif aussucht == "3":
        amount = withdraw(balance)
        balance -= amount
        print(f"{amount:.2f} € wurden ausgezahl.")

    elif aussucht == "4":
        print("Programm beendet.")
        break

    else:
        print("Ungültige Auswahl!")




