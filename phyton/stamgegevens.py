import sqlite3

conn = sqlite3.connect('autoverhuur.sql')
cursor = conn.cursor()

while True:

    print ("1. Merk toevoegen ")
    print ("2. Merk non-actief maken ")
    print ("50. Lijst met merken") 
    print ("99. Stoppen")

    keuze = input("Kies een optie: ")

    if keuze == "1":
        print("")
        merk = input("Voer de naam van het merk in: ")
        sqlBestaat = f"SELECT * FROM Merk WHERE MerkNaam = '{merk}';"
        cursor.execute(sqlBestaat)
        resultaat = cursor.fetchone()
        if resultaat:
            #"Showroom" if auto.SalesAuto == True else "VerhuurAuto"
            print(f"Merk '{merk}' bestaat al. Het merk is niet/wel actief: {resultaat[2]}.")
            print('--------------------------------------------------')
        else:
            sql = f"INSERT INTO Merk (MerkNaam) VALUES ('{merk}');"
            print(f"SQL: {sql}")
            print('--------------------------------------------------') 
            cursor.execute(sql)
            conn.commit()
            print(f"Merk '{merk}' is toegevoegd.")
            print('--------------------------------------------------')
            print("")
    elif keuze == "2":
        print("")
        merk = input("Voer de naam van het merk in dat non-actief gemaakt moet worden: ")
        sqlBestaat = f"SELECT * FROM Merk WHERE MerkNaam = '{merk}';"
        cursor.execute(sqlBestaat)
        resultaat = cursor.fetchone()
        if resultaat:
            sql = f"UPDATE Merk SET MerkActief = false WHERE MerkNaam = '{merk}';"
            print(f"SQL: {sql}")
            print('--------------------------------------------------') 
            cursor.execute(sql)
            conn.commit()
            print(f"Merk '{merk}' is nu non-actief gemaakt.")
            print('--------------------------------------------------')
            print("")
        else:
            print(f"Merk '{merk}' bestaat niet.")
            print('--------------------------------------------------')
    elif keuze == "50":
        sql = "SELECT * FROM Merk where MerkActief = true order by MerkNaam;"
        cursor.execute(sql)
        merken = cursor.fetchall()
        print("")
        print("Lijst met merken:")
        for m in merken:
            print(m[1])
        print('--------------------------------------------------')
        print("")
    elif keuze == "99":
        print("Programma wordt afgesloten.")
        break