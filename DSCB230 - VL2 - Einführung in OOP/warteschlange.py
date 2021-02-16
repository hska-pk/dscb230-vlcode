
class Warteschlange():
    """ Die Klasse bildet eine Warteschlange ähnlich zu der eines Supermarkts ab """

    def __init__(self):
        """ Konstruktor: legt eine leere Warteschlange an """
        self.kunden = [] 

    def ankommen(self, kunde):
        """ Einen Kunden an die Warteschlange anfügen """
        self.kunden.append(kunde) 

    def verlassen(self):
        """ Der nächste Kunde in der Warteschlange verlässt diese und wird von der Methode zurückgegeben """
        if len(self.kunden) > 0:
            kunde = self.kunden.pop(0)
            print(f"{kunde} hat die Warteschlange verlassen")
            return kunde
        else:
            print(f"Kein Kunde in der Warteschlange")
            return None
    
    def ausgabe(self):
        """ Die Warteschlange darstellen """
        print("Warteschlange:")
        for idx, kunde in enumerate(self.kunden):
            print(f"Position {idx}: {kunde}")

class Kunde():
    """ Die Klasse repräsentiert Kunden """

    def __init__(self, vorname, nachname):
        self.vorname = vorname
        self.nachname = nachname

    def __str__(self):
        """ Ausgabe eines Kunden durch Vor- und Nachnamen """
        return f"{self.vorname} {self.nachname}"


w = Warteschlange()  # Objekt von Klasse "Warteschlange" instanziieren 
# einige Kunden "kommen an"
w.ankommen("Peter")
w.ankommen("Julia")
w.ankommen("Manfred")

w.ausgabe()  # Warteschlange anzeigen
w.verlassen()  # der nächste Kunde verlässt die Warteschlange
w.ausgabe()  # Warteschlange anzeigen


w2 = Warteschlange()
w.ankommen(Kunde("Peter", "Müller"))
w.ankommen(Kunde("Julia", "Schulze"))
w.ankommen(Kunde("Manfred", "Mommsen"))
w.ausgabe()