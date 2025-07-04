# Basisvaardigheden in MarkDown


De Heading hierboven is een Heading 1 en wordt aangegeven met één hashtag.
Headings 2 en 3 heeben 2 of 3 hashtags (voorafgaand aan de heading, denk aan de spatie tussen de hashtag(s) en de titel) 
Als je HTML tags wilt weergeven, en niet uit laten voeren kun je deze met backticks omlijsten, beter is het de "code block" functionaliteit te gebruiken: zet drie backticks op een eigen regel, en sluit af met drie backticks op een eigen regel. In een code block hoeven HTML tags niet van een backtick voorzien te worden. 

# Inhoudsopgave
Speciale GitHub feature, geen onderdeel van MarkDown: de table of Contents
Als je meerdere headings in je file hebt maakt GitHub een inhoudsopgave, die te bereiken is met het hamburgermenu rechtsboven

# Line Break
Om een line break in te voegen kun je de HTML tag `</br>` gebruiken, of twee of meer spaties aan het einde van de regel

# Styling
Dit is tevens een voorbeeld van een tabel in Markdown!
|Effect|Syntax| Voorbeeld| Weergave| 
|----|-----|----|----| 
|Bold (**vetgedrukt**)| `**Tekst in bold**` (geen spaties) of `__ Tekst in bold __`|`** Deze tekst wordt vet getoond **`|**Deze tekst wordt vet getoond**| 
|italic(_schuin_)| `* schuine tekst *` of `_ schuine tekst _`|`* Deze tekst wordt schuin getoond *`|*Deze tekst wordt schuin getoond*| 
|Strikethrough(~~Doorgehaald~~)| `~~ doorgehaalde tekst ~~`| `~~ Deze tekst wordt doorgehaald getoond ~~`|~~Deze tekst wordt doorgehaald getoond~~|

Styling kenmerken kunnen genest worden, dus binnen het ene styling element kan een ander styling element worden toegepast
Voorbeeld:</br>
\**Deze tekst is `<ins>extreem</ins>` belangrijk**`</br>
**Deze tekst is <ins>extreem</ins> belangrijk**</br>

De uitlijning van een kolom kan geregeld worden met een dubbele punt in de line separator tussen de heading en de eerste datarow
Zet de dubbele punt vóór de streepjes (:-----) om links uit te lijnen, erachter (--------:) om rechts uit te lijnen, en mocht je onverhoopt willen centreren dan zet je gewoon een dubbele punt voor en achter de streepjes (:--------:)

Met Markdown kun je geen images, lists of HTML tags opnemen in een tabel

# Lists

Dit is een voorbeeld van een unordered list en ordered list
een unordered list kan worden weergegeven met een - * +
een ordered list word weergegeven met een cijfer en spatie(1. 2. 3.)
voorbeeld:

- Mark Rutte
* Rob Lansu
+ Atmaca 

1. George Washington
2. Trump
3. Elon Musk

# Links

``` 
[google zoeken](https://google.com)
```
geeft: </br>
[google zoeken](https://google.com)


