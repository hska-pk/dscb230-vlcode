



def ankommen(w, neuer_kunde):
    """ Hängt einen Kunden an die Warteschlange w (Typ list) an. """
    w.append(neuer_kunde)

def verlassen(w):
    """ der erste Kunde in der Warteschlange wird "entfernt". 
        Gibt den Kunden als Rückgabewert zurück """
    if len(w) > 0:
        kunde = w.pop()  # erster in der Warteschlange
        print(f"{kunde} hat die Warteschlange verlassen")
        return kunde
    else:
        print(f"Kein Kunde in der Warteschlange")

    
def ausgabe(w):
    """ zeigt die Warteschlange an """
    print("Warteschlange:")
    for idx, kunde in enumerate(w):
        print(f"Position {idx}: {kunde}")

warteschlange = []

ankommen(warteschlange, "Peter")
ankommen(warteschlange, "Julia")
ankommen(warteschlange, "Manfred")

ausgabe(warteschlange)  # Warteschlange anzeigen
verlassen(warteschlange)  # der nächste Kunde verlässt die Warteschlange
ausgabe(warteschlange)  # Warteschlange anzeigen

