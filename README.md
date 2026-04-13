# To-Do API 

## Beskrivelse
Prosjektet er en enkel oppgavebehandler hvor brukeren kan holde oversikt over gjøremål. Målet med løsningen er å gjøre det lett å opprette, se, endre og slette oppgaver på en oversiktlig måte. Applikasjonen består av en backend og en frontend som jobber sammen.

## Backend
Backend er laget i Python og fungerer som et API. Den tar imot forespørsler fra frontend og håndterer lagring og henting av data. Dataene lagres enten i en SQLite-database eller i en data.json-fil, som er en enkel måte å lagre informasjon på.

## Frontend
Frontend er laget med HTML og JavaScript. index.html er siden brukeren ser og bruker. JavaScript brukes til å sende forespørsler til backend og oppdatere siden når noe skjer, for eksempel når en ny oppgave blir lagt til eller slettet.

## Forklaring
Når brukeren trykker på knapper eller legger inn tekst, sendes det en forespørsel til backend, som så svarer med oppdatert data. Dette gjør at siden oppdateres uten at man trenger å laste den på nytt.  
Prosjektet viser hvordan man kan lage en enkel webapplikasjon med frontend og backend som kommuniserer med hverandre.

## Hvordan starte backend
For å kjøre backend må du først installere det som trengs og deretter starte serveren.  

Først må du laste ned eller klone prosjektet til maskinen din og åpne mappen i en editor, for eksempel VS Code.  

Deretter kan du lage et virtuelt miljø (valgfritt):

```bash
python -m venv venv
```

```bash
venv\Scripts\activate
```

```bash
pip install flask flask-cors
```

```bash
pip install fastapi uvicorn
```

```bash
python app.py
```

```bash 
uvicorn main:app --reload
```

Når serveren kjører, vil den vanligvis være tilgjengelig på

http://127.0.0.1:8000


## API-et brukes til å håndtere oppgaver i applikasjonen ved at frontend sender forespørsler til backend. For eksempel kan brukeren hente alle oppgaver som er lagret, legge til en ny oppgave ved å skrive inn tekst, oppdatere en eksisterende oppgave eller slette en oppgave. Backend behandler disse forespørslene og sender tilbake oppdatert data, slik at endringene vises direkte i brukergrensesnittet uten at siden må lastes på nytt.