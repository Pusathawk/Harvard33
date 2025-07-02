coda of sqlite
* is alles selecteren

create table 
id integer primary key autoincrement, means id geven met integer getallen, die je niet 
telkens opnieuw hoeft in te voeren

onder de id toevoegen van eigenschappen zoals bij een vlucht origin en destination

data vinden en of uithalen met SELECT

select * ....... means alles selecteren van de kaartenbak

je kan ook selecteren op eigenschappen en of hoofdmappen zoals origin en of destination

examples verschillende soorten selects hieronder:

select * from flights where id = 3;
select * from flights where origin like "%a%"; = hiermee selecteert ie alles bij origin die een letter a bevat

de tag insert= invoegen   for instance: insert to flight (origin, destination, duration,) values ("istanbul", "tokyo", 700);
    
je kan functions toevoegen:
average
count
max
min
sum

update data comment
set wijs je aan bijvoorbeeld de  duration = 720
where functie wijs je aan welke vlucht

set duration= 720
where origin= "Istanbul"
and destionation= "Tokyo";   # met deze teken ; sluit je de update comment

als laatste delete data comment

example:
delete from flights where destijnation= "Tokyo";

other clauses:
limit
order by # deze gebruik je vaak, is sorteren
group by
having

SELECT naam, leeftijd
FROM klanten
ORDER BY leeftijd ASC;

dit geeft een lijst van klanten gesorteerd op leeftijd van jong naar oud

#acs betekent van klein naar groot



    

