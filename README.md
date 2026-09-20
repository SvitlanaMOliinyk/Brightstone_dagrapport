# Dagrapport Brightstone 
## Beschrijving
Dit is een Python CLI tool voor Brightstone Logistics. 
De applicatie leest ordergegevens uit en genereert een dagelijks rapport. 
Het rapport bevat totaal aantal orders, totale omzet, top-5 producten op omzet, top-5 klanten op besteed bedrag, en omzet per categorie aflopend gesorteerd.

## Functionaliteiten
1. CSV-bestanden met ordergegevens inlezen. 
2. Totale omzet berekenen. 
3. Aantal orders bepalen. 
4. Top 5 producten op omzet tonen. 
5. Top 5 klanten op besteed bedrag tonen.
6. Omzet per categorie berekenen.
7. Rapport genereren in Markdown of JSON.
8. Fouten duidelijk melden met logging en specifieke exitcodes.

## Vereisten
- Python 3.14
- pytest 
- mypy
- ruff

## Installatie
Maak een virtual environment aan en activeer deze:
```
python -m venv .venv
.venv\Scripts\activate
```
Installeer daarna de development tools:
```
python -m pip install pytest pytest-cov ruff mypy
```
## Test uitvoeren
```
pytest
```
## Programma uitvoeren
Start het programma met het volgende commando in de terminal:
### Markdown-rapport:
```
 "python -m rapport --input orders.csv --output rapport.md --format markdown"
```
### JSON-rapport:
```
 "python -m rapport --input orders.csv --output rapport.json --format json"
```
## Output
Het programma ondersteunt twee uitvoerformaten:
- Markdown 
- JSON