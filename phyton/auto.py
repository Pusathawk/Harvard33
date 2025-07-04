.0# auto.py
from datetime import date

class Auto:
    def __init__(self, merk, model, kenteken):
        self.merk = merk
        self.model = model
        self.kenteken = kenteken
        
        self.Kilometerstand = 0  # standaard 0 km
        self.TankInhoud = 50
        self.AantalLitersInTank= 15
        self.Verbruik = 5  # verbruik in liters per 100 km  
        self.SalesAuto =True
        self.Aankoopdatum = date.today()  # standaard vandaag

    

    def Rijden(self, AantalKilometers):
        nodig= AantalKilometers * self.Verbruik / 100 #brandstof nodig voor het aantal km
        if self.AantalLitersInTank - nodig < 0:
            print(f"Het is niet mogelijk om {AantalKilometers} kilometer te rijden, er is maar {self.AantalLitersInTank} liter brandstof aanwezig. ")
            print(f"Hiermee kunt u {self.AantalLitersInTank/ self.Verbruik * 100} km rijden")
        else:
            self.AantalLitersInTank -= nodig
            self.Kilometerstand += AantalKilometers
            print(f"We hebben {AantalKilometers} kilometer gereden. We hebben nog {self.AantalLitersInTank:.2f} liter over.")

    def Tanken(self, AantalLiters):
        if self.AantalLitersInTank + AantalLiters > self.TankInhoud:
            print("De tank kan niet zoveel brandstof bevatten!\r\nTanken afgebroken.")
            print(f"De tank kan maximaal {self.TankInhoud} liter bevatten.")
            # self.AantalLitersInTank = self.TankInhoud
        else:
            self.AantalLitersInTank += AantalLiters
            print(f"Er zit nu {self.AantalLitersInTank} liter brandstof in de tank.")

