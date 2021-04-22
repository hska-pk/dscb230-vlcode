

import geometry.shapes.point
p1 = geometry.shapes.point.Point(1, 1)  # Zugriff auf Konstruktor
p2 = geometry.shapes.point.Point(2, 2)  # Zugriff auf Konstruktor
midpoint = geometry.shapes.point.Point.midpoint(p1, p2)  # Zugriff auf statische Methoden
print(midpoint)

import geometry.shapes.point as pt
p1 = pt.Point(1, 1)  # Zugriff auf Konstruktor
p2 = pt.Point(2, 2)  # Zugriff auf Konstruktor
midpoint = pt.Point.midpoint(p1, p2)  # Zugriff auf statische Methoden
print(midpoint)


from geometry.shapes.point import Point
p1 = Point(1, 1)  # Zugriff auf Konstruktor
p2 = Point(2, 2)  # Zugriff auf Konstruktor
midpoint = Point.midpoint(p1, p2)  # Zugriff auf statische Methoden
print(midpoint)


from geometry.shapes.point import Point as Pt
p1 = Pt(1, 1)  # Zugriff auf Konstruktor
p2 = Pt(2, 2)  # Zugriff auf Konstruktor
midpoint = Pt.midpoint(p1, p2)  # Zugriff auf statische Methoden
print(midpoint)

