# imbor_rest
Demo rest api voor imbor ontologie

### Doel
Dit is een demo applicatie voor het implementeren van een REST API gebaseerd op de Open Api Specification 3.0.

![screenshot van de user interface]
(https://github.com/NielsHoffmann/imbor_rest/blob/master/screenshot.png)

Deze applicatie gebruikt de API key die het CROW uitgeeft om sparql queries te doen op het linked data platform van het CROW. 
Deze queries worden ervolgens aangeboden via een rest endpoint.

### Versie
0.1.0 - intitiele opzet oas3 rest api  


### Afhankelijkheden
* Python 3
* flask
* flasgger
* requests
* urllib
* uuid
* hmac
* base64
* hashlib

### Documentatie
De applicatie is een python flask webapp, die gebruik maakt van de [flasgger](https://github.com/flasgger/flasgger) extensie
om een OpenAPI-Specification API te realiseren met een Swagger UI frontend.

Het CROW LDP Endpoint maakt gebruik van een hmac gebaseerd authenticatie mechanisme. In de CrowLdp class wordt de juiste 
authorization header gegenereerd op basis van de keys die in het config bestand staan.

De OtlQueries class bevat alle sparql queries. De imbor_rest bevat de routes voor de API en de API documentatie.

#### Installatie
Maak een python environment aan (met conda of pip...) met de bovengenoemde afhankelijkheden.
Vul je api key gegevens in in het cfg bestand (en verwijs naar het juiste bestand bij het initialiseren van de flask app)
Start de app met het commado `python -m imbor_rest` in de root folder. De swagger ui is dan te vinden op:
 [http://localhost:5000/apidocs](http://localhost:5000/apidocs) 
 
 ### Disclaimer
 Dit is een eerste opzet van een imbor rest api.... Er is nog geen https geimplementeerd. 
 De swagger documentatie kan ongetwijfeld ook nog beter.
 Flask start een development server, er is nog geen werk gedaan om deze app 'productie waardig' te maken...



