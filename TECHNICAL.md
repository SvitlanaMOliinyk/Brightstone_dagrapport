# Technische toelichting 
## Dagrapport Brightstone

### 1. Doel van het programma
Het programma is een Python CLI-tool voor het verwerken van ordergegevens van Brightstone Logistics en het creeren van rapporten.

#### Dree hoofdtaken van het programma:
- ordergegevens uit een csv-bestand lezen,
- de gegevens analyseren en berekeningen uitvoeren,
- een dagelijks rapport genereren in Markdown- of JSON-formaat.

Het rapport bevat totaal aantal orders, totale omzet, top-5 producten op omzet, top-5 klanten op besteed bedrag, en omzet per categorie aflopend gesorteerd.

### 2. Architecture
De applicatie heeft modulaire structuur. Elke modul heeft een eigen verantwoordelijkheid. 
Daardoor blijft code overzichtelijk en kunnen onderdelen onafhankelijk worden getesteerd en aangepast.

De modulen zijn:
- ```cli.py``` verwerkt de argumenten die de gebruiker via cli invoert. Het verplichte argument is het pad naar het inputbestand.
- ```reader.py``` leest een csv-bestand en controleert vereiste kolommen. De gegevens worden omgezet naar een list met dictionaries.
- ```report.py``` bevat logica voor de berekeningen en analyze van de gegevens.
- ```writer.py``` bepaalt gekozen formaat, roept juiste writer en schrijft gegenereerde rapport naar outputbestand.
- ```markdown_writer.py``` genereert het rapport in markdown-formaat.
- ```json_writer.py``` genereert het rapport in json-formaat.
- ```errors.py``` bevat eigen exception classes van de applicatie.
- ```main_.py``` is het entry point van applicatie. Hier worden de onderdelen opgeroepen en worden fouten centraal afgehandeld.

### 3. Ordergegevens
Een order wordt tijdens het verwerken opgeslagen als een dictionary:
```{
    "order_id": "...",
    "datum": "...",
    "klant": "...",
    "product": "...",
    "categorie": "...",
    "aantal": "...",
    "prijs": Decimal("...")
}
```
Voor geldbedragen wordt Decimal gebruikt in plats van float om de problemen met nauwkeurigheid te voorkomen.

De huidige applicatie leest de csv uit het projectbestandssysteem. Wanneer ge gegevens later bijvoorbeeld via een API or een upload binnenkomen kan een extra module worden toegevoegd.
De analyze- en writer-modulen hoeven dan niet aangepast te worden.

### Foutafhandeling
De applicatie gebruikt de standard Python exceptions en twee eigen exeptions:
- ```InvalidCsvError```
- ```MissingColumnError```<br>
De eigen exceptions erven van ```Exception```
De functies signaleren fouten door exceptions te reisen. ```_main_.py```handelt deze fouten centraal af.<br>
Voor de gebruiker wordt een duidelijke foutmelding gelogd en het programma gebruikt een passende exitcode. 

### Testen
Het programma bevat pytest-tests voor:
- CLI-argumenten,
- lezen en valideren van csv-bestand,
- foutafhandeling,
- berekeningen en analyze,
- markdown- en json-output.


