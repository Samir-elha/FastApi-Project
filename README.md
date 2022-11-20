# Film API - Project API-DEVELOPMENT
## Documentatie

- De thema die ik gekozen heb is films, omdat ik graag films kijk. Het leek me een leuke idee om daar een opsplitsing te maken van verschillende genres met daarin meerdere films

#### Links
-	[FastAPI](https://fastapi-samir-elha.cloud.okteto.net/genre "Link FastAPI")
-	[Front-end](https://samir-elha.github.io/ "Front-end")
-	[Repository van front-end](https://github.com/Samir-elha/samir-elha.github.io "Repository van front-end")

## OpenAPI docs
Hieronder heb ik de openapi docs open met uitleg.

<img width="959" alt="image" src="https://user-images.githubusercontent.com/91054513/202922291-3d04e7a3-6be9-4b72-b31e-d14ca289520a.png">

### GET /genre

<img width="731" alt="image" src="https://user-images.githubusercontent.com/91054513/202922456-7719f4d9-3d5a-47e1-8dec-494447adba51.png">


### GET /genre{idS}

<img width="582" alt="image" src="https://user-images.githubusercontent.com/91054513/202922511-a7a58a2e-9f1b-4a7b-b9af-729aca175bb3.png">

### POST /genre

<img width="582" alt="image" src="https://user-images.githubusercontent.com/91054513/202922527-ec970ccf-e457-4e5d-9feb-0cba935baf46.png">

## GET via Postman
Hieronder zie je een eenvoudige get request.

<img width="769" alt="image" src="https://user-images.githubusercontent.com/91054513/202920308-b207a605-3a7f-43fd-bae3-456cf16dc39f.png">

## POST via Postman
### POST
Hieronder wil ik een nieuwe genre toevoegen met nieuwe films, we krijgen de volgende tekst te zien: Genre added succesfully.

<img width="768" alt="image" src="https://user-images.githubusercontent.com/91054513/202920811-c25dce7a-ca70-44f3-901a-84d436169c8d.png">

### GET after POST
Als we een nieuwe get request doen, zien we dat de data goed is gepost.

<img width="770" alt="image" src="https://user-images.githubusercontent.com/91054513/202920457-26ae3f69-a50b-4376-af25-0a79c01c6e29.png">

## Okteto Stack
In de cloud heb ik 2 stacks draaien, een voor mijn api en een MONGODB database.

<img width="913" alt="image" src="https://user-images.githubusercontent.com/91054513/202921751-675586ef-9524-437f-aec9-a0a5f766d376.png">

## Back-end

#### Api.py
API.py bevat het programma met de nodige CORS en get requests.

<img width="623" alt="image" src="https://user-images.githubusercontent.com/91054513/202921689-1ae5739a-863e-40db-8f3a-65323b91d558.png">

#### Model.py
Model.py is voorzien van de nodige models in ons project

<img width="563" alt="image" src="https://user-images.githubusercontent.com/91054513/202921707-aaa973a6-bb88-4bb3-bb2f-79383527ea15.png">


#### Database.py
Database.py zorgt ervoor dat we de database kunnen vullen, updaten en verwijderen

<img width="585" alt="image" src="https://user-images.githubusercontent.com/91054513/202921724-be24fc0d-3e55-44bf-92a8-46752579660c.png">

## Front-End

<img width="960" alt="image" src="https://user-images.githubusercontent.com/91054513/202921805-57eb7e09-3e3f-4921-978d-36bd75f025dc.png">

Op het moment van bekijken front-end, krijgen we 2 genres: Horror en Comdedy met een aantal films. De input field om een film met genre toe te voegen werkt niet.

# Conclusie
De opdracht was erg leerzaam, maar wel zat ik een aantal keer vast bij een error die moeilijk te verhelpen was. Ik heb een werkende api gebouwd met een database op de cloud, die doormiddel van Alpine JS de data verkreeg.




