from auto import Auto

# Lijst om auto's op te slaan
autos = []

def toon_autos(autos):
    """Toont een lijst met ingevoerde auto's."""
    if not autos:
        print("Er zijn nog geen auto's toegevoegd!")
    else:
        for i, auto in enumerate(autos):
            # if auto.SalesAuto:
            # expression_if_true if condition else expression_if_false
            print(f"{i + 1}. {auto.merk} {auto.model} ({'Showroom' if auto.SalesAuto else 'VerhuurAuto'}, Kenteken: {auto.kenteken}, KM-stand: {auto.Kilometerstand} km, Liters in auto: {auto.AantalLitersInTank}L, Tankcapaciteit: {auto.TankInhoud}L, Verbruik: {auto.Verbruik}L/100km, Actieradius: {auto.AantalLitersInTank / auto.Verbruik * 100:.1f} km, Aankoopdatum: {auto.Aankoopdatum})")

while True:
    print("\nMenu:")
    print("1. Auto toevoegen")
    print("2. Auto laten rijden")
    print("3. Auto tanken")
    print("4. Verhuur/Sales status wijzigen")
    print("5. Kilometerstand handmatig wijzigen")
    print("8. Kenteken wijzigen")
    print("11. verbruik wijzigen")
    print("12. Tankinhoud wijzigen")
    print("13. Aankoopdatum wijzigen")
    print("99. Programma beëindigen")

    keuze = input("Maak een keuze: ")

    if keuze == "1":
        # Auto toevoegen
        merk = input("Voer het merk van de auto in: ")
        model = input("Voer het model van de auto in: ")
        kenteken = input("Voer het kenteken van de auto in: ")
        nieuwe_auto = Auto(merk, model, kenteken)
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
        else:
            print("Er zijn geen auto's om te tanken.")
    elif keuze == "4":
        # Verhuur/Sales status wijzigen
        toon_autos(autos)
        if autos:
            auto_index = int(input("Kies een auto (nummer): ")) - 1
            if 0 <= auto_index < len(autos):
                status = input("Is de auto te koop? (ja/nee): ").strip().lower()
                if status == "ja":
                    autos[auto_index].SalesAuto = True
                    print(f"Auto {autos[auto_index].merk} {autos[auto_index].model} is nu te koop.")
                elif status == "nee":
                    autos[auto_index].SalesAuto = False
                    print(f"Auto {autos[auto_index].merk} {autos[auto_index].model} is een huurauto.")
                else:
                    print("Ongeldige invoer.")
            else:
                print("Ongeldige keuze.")

    elif keuze == "5":
        toon_autos(autos)
        if autos:
            auto_index = int(input("Kies een auto (nummer): ")) - 1
            if 0 <= auto_index < len(autos):
                try:
                    nieuwe_km = int(input("Voer de nieuwe kilometerstand in: "))
                    if nieuwe_km >= autos[auto_index].Kilometerstand:
                        autos[auto_index].Kilometerstand = nieuwe_km
                        print(f"Kilometerstand van {autos[auto_index].merk} {autos[auto_index].model} is gewijzigd naar {nieuwe_km} km.")
                    else:
                        print("Nieuwe kilometerstand mag niet lager zijn dan de huidige.")
                except ValueError:
                    print("Ongeldige invoer. Gebruik een geheel getal.")
            else:
                print("Ongeldige keuze.")
        else:
            print("Er zijn geen auto's om te wijzigen.")

    elif keuze == "8":
        toon_autos(autos)
        if autos:
            auto_index = int(input("Kies een auto (nummer): ")) - 1
            if 0 <= auto_index < len(autos):
                nieuw_kenteken = input("Voer het nieuwe kenteken in: ")
                autos[auto_index].kenteken = nieuw_kenteken
                print(f"Kenteken van {autos[auto_index].merk} {autos[auto_index].model} is gewijzigd naar {nieuw_kenteken}.")
            else:
                print("Ongeldige keuze.")
        else:
            print("Er zijn geen auto's om te wijzigen.")
        
    elif keuze == "11":
       toon_autos(autos)
       if autos:
            auto_index = int(input("Kies een auto (nummer): ")) - 1
            if 0 <= auto_index < len(autos):
                liters= int(input("wat is de verbruik van de auto per 100km? "))
                autos[auto_index].Verbruik=liters
                toon_autos(autos)
            else:
                print("ongeldige keuze.")

    elif keuze == "12":
        toon_autos(autos)
        if autos:
            auto_index = int(input("Kies een auto (nummer): ")) - 1
            if 0 <= auto_index < len(autos):
                try:
                    nieuwe_tankinhoud = float(input("Voer de nieuwe tankinhoud in (in liters): "))
                    if nieuwe_tankinhoud > 0:
                        autos[auto_index].TankInhoud = nieuwe_tankinhoud
                        print(f"Tankinhoud van {autos[auto_index].merk} {autos[auto_index].model} is gewijzigd naar {nieuwe_tankinhoud} liter.")
                    else:
                        print("Tankinhoud moet groter zijn dan 0.")
                except ValueError:
                    print("Ongeldige invoer. Gebruik een getal.")
            else:
                print("Ongeldige keuze.")
        else:
            print("Er zijn geen auto's om te wijzigen.")

    elif keuze == "13":
        toon_autos(autos)
        if autos:
            auto_index = int(input("Kies een auto (nummer): ")) - 1
            if 0 <= auto_index < len(autos):
                nieuwe_datum_str = input("Voer de nieuwe aankoopdatum in (YYYY-MM-DD): ")
                try:
                    from datetime import datetime
                    nieuwe_datum = datetime.strptime(nieuwe_datum_str, "%Y-%m-%d").date()
                    autos[auto_index].Aankoopdatum = nieuwe_datum
                    print(f"Aankoopdatum van {autos[auto_index].merk} {autos[auto_index].model} is gewijzigd naar {nieuwe_datum}.")
                except ValueError:
                    print("Ongeldige datum. Gebruik het formaat YYYY-MM-DD.")
            else:
                print("Ongeldige keuze.")
        else:
            print("Er zijn geen auto's om te wijzigen.")
             

               

      
          

            
    elif keuze == "99":
        # Programma beëindige
        print("Programma beëindigd.")
        break
    else:
        print("Ongeldige keuze, probeer opnieuw.")
