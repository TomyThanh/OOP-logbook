#Statische Klassen
from abc import ABC, abstractmethod

#Eine Statische Klasse ist wie eine Werkzeug-Kiste mit Funktionen/Methoden. Also es bewahrt sie auf.
#Deswegen braucht man kein self in den Parameter der Funktionen.
#Man ruft die Methoden direkt mit dem Klassennamen auf und der Punktnotation: Mathe.addieren(1+1)

class Mathe(ABC):

    pi = 3.14

    @staticmethod
    def addieren(a,b):
        return a + b
    
    @staticmethod
    def subtrahieren(a,b):
        return a - b
    
    @staticmethod
    def multiplizieren(a,b):
        return a * b
    
    @staticmethod
    def dividieren(a,b):
        return a / b
    
    @staticmethod
    def kreisflaecheBerechnen(radius):
        return Mathe.pi * radius ** 2
    
    @abstractmethod #Damit verhindert man, dass ein Objekt mit dieser Klasse erstellt wird.
    def dummy():
        pass
