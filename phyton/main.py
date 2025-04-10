from auto import Auto

# Lijst om auto's op te slaan
autos = []

def toon_autos(autos):
    """Toont een lijst met ingevoerde auto's."""
    if not autos:
        print("Er zijn nog geen auto's toegevoegd!")
    else:
        for i, auto in enumerate(autos):
            print(f"{i + 1}. {auto.merk} {auto.model} (Liters in auto: {auto.AantalLitersInTank}, Brandstof verbruik:  {auto.Verbruik}L/100km, Actieradius: {auto.AantalLitersInTank/auto.Verbruik*100}km)")

while True:
    print("\nMenu:")
    print("1. Auto toevoegen")
    print("2. Auto laten rijden")
    print("3. Auto tanken")
    print("4. Verhuur/Sales status wijzigen")
    print("99. Programma beëindigen")

    keuze = input("Maak een keuze: ")

    if keuze == "1":
        # Auto toevoegen
        merk = input("Voer het merk van de auto in: ")
        model = input("Voer het model van de auto in: ")
        nieuwe_auto = Auto(merk, model)
        autos.append(nieuwe_auto)
        print(f"Auto {merk} {model} is toegevoegd.")
    elif keuze == "2":
        # Auto laten rijden
        toon_autos(autos)
        if autos:
            auto_index = int(input("Kies een auto (nummer): ")) - 1
            if 0 <= auto_index < len(autos):
                afstand = float(input("Hoeveel kilometer wil je rijden? "))
                autos[auto_index].Rijden(afstand)
            else:
                print("Ongeldige keuze.")   
    elif keuze == "3":
        # Auto tanken
        toon_autos(autos)
        if autos:
            auto_index = int(input("Kies een auto (nummer): ")) - 1
            if 0 <= auto_index < len(autos):
                liters = float(input("Hoeveel liters wil je tanken? "))
                autos[auto_index].Tanken(liters)
            else:
                print("Ongeldige keuze.")
    elif keuze == "99":
        # Programma beëindige
        print("Programma beëindigd.")
        break
    else:
        print("Ongeldige keuze, probeer opnieuw.")
