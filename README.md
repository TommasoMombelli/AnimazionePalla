# installazione del software python: Server

## Descrizione
Questo software genera un QrCode che mostra l'indirizzo IP del Server e permette la connessione del client (app flutter). Inoltre legge le coordinate della posizione inviate dal client e permette il movimento della pallina mostrando quando viene vinto il "gioco". 


## Installation

### Prerequisites
- VSC con l'estensione di Python installata
- pacchetty Python necessari

### Steps
1. scaricare la repository da GitHub:
   ```bash
   git clone https://github.com/TommasoMombelli/AnimazionePalla.git

2. aprire la cartella in cui è salvato il progetto e utilizzare il comando
    ```bash
    cmd
   nella linea in cui è specificato il percorso

3. Creazione dell'envinroment:
   nel terminal che si è aperto creare l'environment tramite il comando
   ```bash
   python -m venv remote_ball
   NB: al posto di "remote_ball" si può usare il nome che si preferisce

4. attivazione dell'environment:
   ```bash
   remote_ball\Scripts\activate.bat
   NB: oppure al posto di remote_ball il nome dato all'environment

5. installare i pacchetti python necessari:
   ```bash
   python -m pip install -r .\requirements.txt

6. lanciare il programma:
   ```bash
   python Server.py
   
