class auto:
	def __init__ (self, merk, model):
		self.merk = merk
		self.model = model

	TankInhoud = 50
	Brandstof = 10
	Verbruik = 5

	def Rijden(self, AantalKilometers):
		if (self.Brandstof - AantalKilometers*self.Verbruik/100) < 0:
			print (f"Het is niet mogelijk om {AantalKilometers} kilomter te rijden, er is maar {self.Brandstof} aanwezig" )
		else:
			self.Brandstof = self.Brandstof - AantalKilometers*self.Verbruik/100
			print (f"We hebben {AantalKilometers} kilometer gereden, we hebben nog {self.Brandstof} liter over")

	def Tanken(self, AantlLiters):
		self.Brandstof = self.Brandstof + AantlLiters
		print (f"Er zit nu {self.Brandstof} liters in de tank")


Auto1 =auto("Mercedes", "190")
Auto2 =auto("Opel", "Kadet")
Auto3 = auto("Simca", "1100")

print (Auto1.merk)
print(Auto1.model)
Auto1.TankInhoud = 75
Auto1.Verbruik = 10
print(Auto1.TankInhoud)
print(Auto1.Verbruik)
Auto1.Rijden(150)
Auto1.Tanken(20)
Auto1.Rijden(150)







