# back-end-test

back-end test api

## Coses a tenir en compte

Tot i que no té gaire sentit en un exemple tant petit, ja que l'enunciat demana fer servir OO patterns, he afegit
la classe Transaction per gestionar les transaccions a mode d'exemple.

Tampoc queda massa clar d'on treure les dades que retorna la API. He optat per utilitzar la "dummy data" que hi ha
a l'enunciat.

## ENDPOINTS

### /

Hello world. Per comprovar que la API està funcionant

### /currency_rates

Retorna tots els currency rates

### /currency_rate

Retorna el currency rate passant com a paràmetres els valors from i to. Exemple:
/currency_rate?from=EUR&to=USD

### /transactions

Retorna totes les transaccions passant com a paràmetres la currency i, opcionalment, l'sku. Exemples:

/transactions?currency=USD  
/transactions?currency=USD&sku=T2006

## Per posar en marxa la API:

### Amb Docker (recomanat)

1 - Construir la imatge
docker build -t flask-rest-api .

2 - Iniciar el contenidor
docker run -d -p 5000:5000 flask-rest-api

3 - Accedir a la URL http://localhost:5000 per comprovar que es rep el missatge "Hello world"

### Sense Docker

1 - Crear entorn virtual i instal·lar dependències:
python -m venv venv
venv/Scripts/activate
pip install -r requirements.txt

2 - Per executar els testos:
python test.py

3 - Per iniciar la API
flask run

4 - Accedir a la URL http://localhost:5000 per comprovar que es rep el missatge "Hello world"
