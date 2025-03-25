# Cheat Sheet Python

## Basis Syntax
functie
def HelloWorld(Naam):
    print (f"Hallo Wereld, welkom {Naam}")

if
if b>a:
    doe dit
elif a==b:
    doe iets anders
else:
    geef het op

## Lists
Een nieuwe lege list
AppelKist = []

Toevoegen aan een list
AppelKist.append(object)

Aantal items in een list
len(AppelKist)

## Loops
for x in AppelKist: 
    print(x)

for x in range(10)
    print(x*x)

while Functie < 10:
    Onderdelen()
    Functie = int( input("Geef een functie: "))
    Programma(Functie)

## Modules (Code bibliotheek)
Een module is een Python bestand met (Python) functies, bijvoorbeeld ScriptaFuncties.py
Om deze functies te gebruiken geef je een import statement:
import ScriptaFuncties
En vervolgens roep je een functie aan:
ScriptaFuncties.HelloWorld("Rob")
response:
Hallo Wereld, welkom Rob
