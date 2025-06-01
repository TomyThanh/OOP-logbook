#Klassenmethoden & Fabrikmethoden

class Datum:
    def __init__(self, tag, monat, jahr):
        self.tag = tag
        self.monat = monat
        self.jahr = jahr
    
    #Ein Entwurfsmuster mit dem man mit allen Dtypes arbeiten kann, als Argumente (also strings und integers)
    @staticmethod #Fabrikmethode übergibt die Werte an den Konstruktor __init__ 
    def vonString(datumStr: str): #Somit erstellt die Fabrikmethode ein Objekt in einer Klassen 
        tag, monat, jahr = map(int, datumStr.split("-")) #ABER Fabrikmethoden berücksichtigen nicht von welcher Klasse sie aufgerufen werden
        return Datum(tag,monat,jahr) #Fabrikmethoden sind UNIVERSELL
    


    @classmethod  #Klassenmethoden berücksichtigen von welcher Klasse die Methoden aufgerufen werden
    def vonStringCLS(cls, datumStr: str): #Passiert das selbe wie bei der Fabrikmethode
        tag, monat, jahr = map(int, datumStr.split("-")) #Man hat aber Zugang zur Klasse
        return cls(tag,monat,jahr)



    def __str__(self):
        return f"{self.tag}.{self.monat}.{self.jahr}"
    
datum = Datum(23,7,2025)
print(datum)

datum2 = Datum.vonString("30-11-1991")
print(datum2)

class DatumMitZeit(Datum):

    def __init__(self, tag, monat, jahr, stunde = 0, minute = 0):
        super().__init__(tag, monat, jahr)
        self.stunde = stunde
        self.minute = minute
    

    @classmethod  #Klassenmethode
    def vonStringCLS(cls, datumStr: str): #Passiert das selbe wie bei der Fabrikmethode
        tag, monat, jahr, stunde, minute = map(int, datumStr.split("-")) #Man hat aber Zugang zur Klasse
        return cls(tag,monat,jahr, stunde,minute)


    def __str__(self):
        return f"{super().__str__()} {self.stunde}:{self.minute}"

datumMitZeit1 = DatumMitZeit.vonString("30-11-1991")
print(datumMitZeit1)

datumMitZeit2 = DatumMitZeit.vonStringCLS("30-11-1991")
print(datumMitZeit2)

