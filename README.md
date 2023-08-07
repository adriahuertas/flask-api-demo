# back-end-test
back-end test api

## Coses a tenir en compte

Tot i que no té gaire sentit en un exemple tant petit, ja que l'enunciat demana fer servir OO patterns, he afegit
la classe Transaction per gestionar les transaccions a mode d'exemple.

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