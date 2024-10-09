import socket
import struct

def client_program():
    host = "10.243.30.87"  # IP del server (PC di Ilaria)
    port = 5000  # Porta del server

    client_socket = socket.socket()  # Istanzia il socket
    client_socket.connect((host, port))  # Connetti al server

    # Richiedi due variabili intere all'utente
    x = int(input("Inserisci il valore di x: "))
    y = int(input("Inserisci il valore di y: "))

    # Impacchetta le due variabili intere in un formato binario usando struct
    message = struct.pack('ii', x, y)

    # Invia le variabili impacchettate al server
    client_socket.send(message)

    # # Attendi la risposta dal server (opzionale)
    # data = client_socket.recv(1024)  # Ricevi i dati (fino a 1024 byte)
    # result = struct.unpack('i', data)[0]  # Decodifica l'intero ricevuto

    # print(f"Risultato ricevuto dal server: {result}")  # Mostra il risultato

    client_socket.close()  # Chiudi la connessione


if __name__ == '__main__':
    client_program()
