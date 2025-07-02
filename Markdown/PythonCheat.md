# Cheat Sheet Python

## Basis Syntax
** functie **</br>
def HelloWorld(Naam):</br>
    print (f"Hallo Wereld, welkom {Naam}")</br>

**if**</br>
if b>a:</br>
    doe dit</br>
elif a==b:</br>
    doe iets anders</br>
else:</br>
    geef het op</br>

**Een inline if:**
expression_if_true if condition else expression_if_false
"Showroom" if auto.SalesAuto == True else "VerhuurAuto"

## Lists
**Een nieuwe lege list**</br>
AppelKist = []</br>
</br>

**Toevoegen aan een list**</br>
AppelKist.append(object)</br>
</br>

**Aantal items in een list**</br>
len(AppelKist)</br>

## Loops
for x in AppelKist:</br> 
    print(x)</br>
</br>
for x in range(10)</br>
    print(x*x)</br>
</br>
while Functie < 10:</br>
    Onderdelen()</br>
    Functie = int( input("Geef een functie: "))</br>
    Programma(Functie)</br>

## Modules (Code bibliotheek)
Een module is een Python bestand met (Python) functies, bijvoorbeeld ScriptaFuncties.py</br>
Om deze functies te gebruiken geef je een import statement:</br>
import ScriptaFuncties</br>
En vervolgens roep je een functie aan:</br>
ScriptaFuncties.HelloWorld("Rob")</br>
response:</br>
Hallo Wereld, welkom Rob</br>
