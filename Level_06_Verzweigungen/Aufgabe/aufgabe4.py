#Aufgabe 4: Taschenrechner

erste_zahl= int(input("bitte geben Sie erste Zahl ein: "))
zweite_zahl= int(input("bitte geben Sie zweite Zahl ein: "))
operation= "+, -, *, /"
operation_mul ="*"
operation_div= "/"
operation_min= "-"
operation_add= "+"
benutzer_operation= input(f"Bitte Geben Sie ein von {operation} ein")

Fehler=" Division durch 0 ist nicht erlaubt. "

if  benutzer_operation ==operation_mul or benutzer_operation ==operation_div or benutzer_operation ==operation_min or benutzer_operation ==operation_add :


 if benutzer_operation==operation_add:    #Grundrechenarten
    print(zweite_zahl+erste_zahl)

 if benutzer_operation==operation_min:
    print(zweite_zahl-erste_zahl)

 if benutzer_operation==operation_mul:
    print(zweite_zahl*erste_zahl)

    #if zweite_zahl==0 and benutzer_operation==operation_div:
     # print(erste_zahl/zweite_zahl)
     #else:
     #print("Fehler: Division durch 0 ist nicht erlaubt.")

 if zweite_zahl==0 and benutzer_operation==operation_div:
    print("Fehler: Division durch 0 ist nicht erlaubt.")

 elif benutzer_operation==operation_div :
    print(erste_zahl/zweite_zahl)
else:
    print(f"Unbekannte Operation:{benutzer_operation}")

