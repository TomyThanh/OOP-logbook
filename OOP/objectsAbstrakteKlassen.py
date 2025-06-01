# Abstrakte Klassen
from abc import ABC, abstractmethod



class Form(ABC): #Man kann kein Objekt mit Klasse Form() erstellen.
    def _init_(self):
        pass

    @abstractmethod # Regel, dass diese berechneFlaeche Funktion da sein muss in den Kind-Klassen
    def berechneFlaeche(self):
        print("Hallo von der Form Klasse")
        

class Rechteck(Form):

    def _init_(self, laenge, breite):
        self.laenge = laenge
        self.breite = breite

    def _str_(self):
        return f"Rechteck mit Fläche {self.berechneFlaeche()}"
    

class Kreis(Form):
    def _init_(self, radius):
        self.radius = radius

    def _str_(self):
        return f"Kreis mit Fläche {self.berechneFlaeche()}"
    
    def berechneFlaeche(self):
        return 3.14 * self.radius ** 2


r1 = Rechteck()
k1 = Kreis()
r1.berechneFlaeche(3,4)
k1.berechneFlaeche(23)


# MIT Polymorphismus kann man Funktionen der Kindklassen überschreiben, so dass sie nicht vererben von der Elternklasse
# Kindklassen ohne Polymorphismus erben weiterhin von der Elternklasse
# MIT Abstrakten Klassen (abc-Modul) kann man verhindern, dass die Elternklasse genutzt wird und Regel für die Kindklassen setzen