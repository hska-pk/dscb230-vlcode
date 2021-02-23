
class Spielkarte():
    """ Klasse zur Repräsentation von Spielkarten """
    
    # def __init__(self):
    #     """ Konstruktor für eine "Standardkarte" (kreuz as) """
    #     self.farbe = "kreuz"
    #     self.wert = "as"


    # def __init__(self, farbe, wert):
    #     """ Konstruktor für eine Karte mit übergebenen Argumenten
    #         für farbe und wert """
    #     self.farbe = farbe
    #     self.wert = wert


    def __init__(self, farbe='kreuz', wert='as'):
        """ Konstruktor für eine Karte mit übergebenen Argumenten
            für farbe und wert. Werden keine Daten übergeben, dann
            wird ein "kreuz as" angelegt  """
        self.farbe = farbe
        self.wert = wert


    def drucken(self):
        """ Gibt Farbe und Werte auf der Konsole aus """
        print(f"Spielkarte mit {self.farbe} - {self.wert}")


    def aendern(self, farbe, wert):
        """ Ändere die Kartenattribute
            positional --> beide Parameter sind zu übergeben """
        self.farbe = farbe
        self.wert = wert

    # def aendern(self, farbe=None, wert=None):
    #     """ Ändere die Kartenattribute
    #         named --> beide Parameter können übergeben werden (sonst Standard) """
    #     self.farbe = farbe
    #     self.wert = wert

    # def aendern(self, farbe, wert=None):
    #     """ Ändere die Kartenattribute
    #         farbe positional --> muss übergeben werden
    #         wert named --> kann übergeben werden (sonst Standard) """
    #     self.farbe = farbe
    #     self.wert = wert

k1 = Spielkarte()
k1.farbe = "kreuz"
k1.wert = "as"


k2 = Spielkarte()
k2.farbe = "karo"
k2.wert = "10"

k1.drucken()
k2.drucken()

k3 = k2
k3.drucken()

k4 = Spielkarte()
k5 = Spielkarte('pik', '7')
k4.drucken()
k5.drucken()

import random

class Spielkarte2():
    """ Klasse zur Repräsentation von Spielkarten (v2) """

    def __init__(self, farbe='kreuz', wert='as'):
        """ Konstruktor für eine Karte mit übergebenen Argumenten
            für farbe und wert. Werden keine Daten übergeben, dann
            wird ein "kreuz as" angelegt  """
        self._farbe = farbe  # Markieren als privates Attribut
        self._wert = wert # Markieren als privates Attribut

    def __str__(self):
        return f"Spielkarte mit Farbe {self.farbe} und Werte {self.wert}"

    def __eq__(self, other):
        """ logische Prüfung auf Gleichheit von zwei Spielkarten """
        return self.farbe == other.farbe and self.wert == other.wert

    @property
    def farbe(self):
        """ get-Methode von Attribut farbe """
        print("getter von farbe aufgerufen")
        return self._farbe

    @property
    def wert(self):
        """ get-Methode von Attribut wert """
        print("getter von wert aufgerufen")
        return self._wert

    @farbe.setter
    def farbe(self, value):
        print("setter von farbe aufgerufen")
        self._farbe = value

    @wert.setter
    def wert(self, value):
        print("setter von wert aufgerufen")
        self._wert = value

    def drucken(self):
        """ gibt den String der Spielkarte auf der Konsole aus """
        print(self)

    @staticmethod
    def zufallskarte():
        """ erzeugt eine zufällige Spielkarte """
        farben = ['kreuz', 'pik', 'karo', 'herz']
        zufallsfarbe = random.choice(farben)  # ziehe zufällige Farbe
        werte = [7, 8, 9, 10, 'bube', 'dame', 'koenig', 'as']
        zufallswert = random.choice(werte)  # ziehe zufälligen Wert
        return Spielkarte(zufallsfarbe, zufallswert)



    


    

# getter/setter ermöglichen folgenden Code:
neuekarte = Spielkarte2()
print(neuekarte.farbe) # Zugriff über get-Methode
neuekarte.farbe = 'karo'  # Zugriff über set-Methode
    
print(neuekarte)
print(f"Spielkarte mit Farbe {neuekarte.farbe} und Werte {neuekarte.wert}")
print(neuekarte)
neuekarte.drucken()

neuekarte2 = Spielkarte2()  # kreuz as
neuekarte3 = Spielkarte2()  # kreuz as
print(neuekarte2 == neuekarte3)  # liefert False! (True nach Programmierung von __eq__)

print(neuekarte2 == neuekarte3)  # liefert True nach Programmierung von __eq__
print(neuekarte2 != neuekarte3)  # liefert False nach Programmierung von __eq__
print(neuekarte2 is neuekarte3)  # liefert False!

x1 = [10, 20, 30] 
x2 = [10, 20, 30] 
print(f"Is x1 == x2? {x1 == x2}")  # liefert True!
x3 = x1
print(f"Result of 'x1 is x2'? {x1 is x2}")  # liefert False!
print(f"Result of 'x1 is x3'? {x1 is x3}")  # liefert True!
    
    
zufallskarte = Spielkarte2.zufallskarte()
zufallskarte.drucken()




class Kartenspiel():
    """ Klasse, die ein Standard-Kartenspiel enthält """

    def __init__(self):
        """ Konstruktor: legt ein Standard-Kartenspiel an """
        farben = ['kreuz', 'pik', 'karo', 'herz']
        werte = [7, 8, 9, 10, 'bube', 'dame', 'koenig', 'as']

        self._spielkarten = []  # Liste mit allen Spielkarten im Spiel
        for f in farben:
            for w in werte:
                self._spielkarten.append(Spielkarte2(farbe=f, wert=w))

    def __iter__(self):
        """ Initialisiert den Iterator """
        self._i = 0  # Initalisierung des Iterators (Startindex 0)
        return self
    
    def __next__(self):
        """ Liefert die nächste Karte bis zum Ende der Liste """ 
        if self._i < len(self._spielkarten):
            karte = self._spielkarten[self._i]
            self._i += 1
            return karte
        else:
            raise StopIteration()


# Verwendung des Iterators in einer for-Schleife
spiel = Kartenspiel()
for karte in spiel:
    karte.drucken()