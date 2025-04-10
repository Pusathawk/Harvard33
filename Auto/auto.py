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










