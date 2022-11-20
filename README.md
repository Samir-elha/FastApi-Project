# Film API - Project API-DEVELOPMENT
## Documentatie

- De thema die ik gekozen heb is films, omdat ik graag films kijk. Het leek me een leuke idee om daar een opsplitsing te maken van verschillende genres met daarin meerdere films

#### Links
-	[FastAPI](https://fastapi-samir-elha.cloud.okteto.net/genre "Link FastAPI")
-	[Front-end](https://samir-elha.github.io/ "Front-end")
-	[Repository van front-end](https://github.com/Samir-elha/samir-elha.github.io "Repository van front-end")

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

<img width="546" alt="image" src="https://user-images.githubusercontent.com/91054513/202920939-4d330bc1-2b83-47a5-8bc6-c25c6cf56426.png">

## Back-end

#### Api.py
API.py bevat het programma met de nodige CORS en get requests.

<img width="182" alt="image" src="https://user-images.githubusercontent.com/91054513/202921191-443e22bd-13a4-47c2-9bbc-94a8609c3a37.png">

#### Model.py
Model.py is voorzien van de nodige models in ons project

<img width="337" alt="image" src="https://user-images.githubusercontent.com/91054513/202921476-2565f179-593f-47e6-86eb-1645f581c91a.png">


#### Database.py
Database.py zorgt ervoor dat we de database kunnen vullen, updaten en verwijderen

<img width="274" alt="image" src="https://user-images.githubusercontent.com/91054513/202921625-d90128e9-81d9-4234-8343-4297061c7734.png">


