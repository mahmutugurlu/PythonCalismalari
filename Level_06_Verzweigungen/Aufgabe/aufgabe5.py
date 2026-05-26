#Aufgabe 5: Wochentag-Programm (match-case)


status = input("Könnten Sie einen Tag eingeben (Montag,Dienstag, Mittwoch,Donnerstag,Freitag, Samstag,Sonntag): ")
match status:
    case "Montag":
        print("Werktag – viel Erfolg!")
    case "Dienstag":
        print("Werktag – viel Erfolg!")
    case "Mittwoch":
        print("Werktag – viel Erfolg!")
    case "Donnerstag":
        print("Werktag – viel Erfolg!")
    case "Freitag":
        print("Werktag – viel Erfolg!")
    case "Samstag":
        print("Samstag – genieß das Wochenende!")
    case "Sonntag":
        print("Sonntag – genieß das Wochenende!")
    case _:     # _ ist der Default-Case, greift wenn kein anderer case passt (wie else)
        print(f"Unbekannter Bestellstatus: '{status}'")