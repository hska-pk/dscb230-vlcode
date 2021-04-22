import point
p1 = point.Point(1, 1)  # Zugriff auf Konstruktor
p2 = point.Point(2, 2)  # Zugriff auf Konstruktor
midpoint = point.Point.midpoint(p1, p2)  # Zugriff auf statische Methoden
print(midpoint)

import point as pt
p1 = pt.Point(1, 1)  # Zugriff auf Konstruktor
p2 = pt.Point(2, 2)  # Zugriff auf Konstruktor
midpoint = pt.Point.midpoint(p1, p2)  # Zugriff auf statische Methoden
print(midpoint)


from point import Point
p1 = Point(1, 1)  # Zugriff auf Konstruktor
p2 = Point(2, 2)  # Zugriff auf Konstruktor
midpoint = Point.midpoint(p1, p2)  # Zugriff auf statische Methoden
print(midpoint)


from point import Point as Pt
p1 = Pt(1, 1)  # Zugriff auf Konstruktor
p2 = Pt(2, 2)  # Zugriff auf Konstruktor
midpoint = Pt.midpoint(p1, p2)  # Zugriff auf statische Methoden
print(midpoint)