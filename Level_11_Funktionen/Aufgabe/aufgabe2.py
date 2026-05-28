#Aufgabe 2: Einheitenumrechner

nutzereingabe = float(input("Bitte gib eine  Zahl an: "))

def km_zu_meilen(km):
    """ Meilen berechnet"""

    return km *  0.621371


def kg_zu_pfund(kg):
    """ Pfund berechnet"""

    return kg *  2.20462


def kmh_zu_ms(kmh):
    """ MS berechnet"""

    return kmh * 1/3.6


def ms_zu_kmh(ms):
    """ KM berechnet"""

    return ms *  3.6



#hauptprogram

print(f"Wert eingeben:{nutzereingabe}")
print(f"{nutzereingabe} KM {km_zu_meilen(nutzereingabe)}")
print(f"{nutzereingabe} KG {kg_zu_pfund(nutzereingabe)}")
print(f"{nutzereingabe} KMH {kmh_zu_ms(nutzereingabe)}")
print(f"{nutzereingabe} MS {ms_zu_kmh(nutzereingabe)}")







