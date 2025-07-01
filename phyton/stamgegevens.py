import sqlite3

conn = sqlite3.connect('autoverhuur.sql')
cursor = conn.cursor()

""""
#**
print(conn)


#**/
"""
while True:

    print ("1. Merk toevoegen ")
    print ("50. Lijst met merken") 
    print ("99. Stoppen")

    keuze = input("Kies een optie: ")

    if keuze == "1":
        merk = input("Voer de naam van het merk in: ")
        sql = f"INSERT INTO Merk (MerkNaam) VALUES ('{merk}');"
        cursor.execute(sql)
        conn.commit()
        print(f"Merk '{merk}' is toegevoegd.")
        print('--------------------------------------------------')
        print("")
    elif keuze == "50":
        sql = "SELECT * FROM Merk order by MerkNaam;"
        cursor.execute(sql)
        merken = cursor.fetchall()
        print("Lijst met merken:")
        for m in merken:
            print(m[1])
        print('--------------------------------------------------')
        print("")
    elif keuze == "99":
        print("Programma wordt afgesloten.")
        break