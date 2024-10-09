import socket
import struct  # Per la gestione di variabili binarie

from tkinter import *
import time

#creazione canvas
root = Tk()
root.title("Ball Animation")

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

print("Larghezza della finestra:", screen_width)
print("Altezza della finestra:", screen_height)

x_max=screen_width
y_max=screen_height


pos_x = 100
pos_y = 100

canvas = Canvas(root, height= y_max, width= x_max)
canvas.pack()

# creazione palla
ball = canvas.create_oval(10, 10, 50, 50, fill="blue")

# movimento palla
canvas.moveto(ball, pos_x, pos_y)
canvas.update()

def move_ball_to(x_nuovo, y_nuovo):
    x, y = canvas.coords(ball)[:2]
    canvas.moveto(ball, x_nuovo, y_nuovo)
    canvas.update()
    time.sleep(0.01)
    x, y = canvas.coords(ball)[:2]


while True:
    move_ball_to()
    again = int(input("Vuoi muovere di nuovo la palla? (1 per sì, 0 per no): "))
    if again != 1:
        final_pos = canvas.coords(ball)
        break

root.mainloop()

# Supponiamo che moveball() sia già definita
def moveball(x, y):
    print(f"Moveball chiamata con x = {x}, y = {y}")
    # Logica di moveball qui (o lascia vuoto se non deve fare nulla in questo esempio)

def server_program():
    # Ottieni l'hostname
    host = socket.gethostname()
    port = 5000  # Porta di ascolto sopra 1024

    server_socket = socket.socket()  # Crea un'istanza del socket
    server_socket.bind((host, port))  # Associa l'host e la porta

    # Configura il numero massimo di client in attesa
    server_socket.listen(1)
    print(f"Server in attesa di connessioni su {host}:{port}...")
    conn, address = server_socket.accept()  # Accetta una nuova connessione
    print("Connessione stabilita con: " + str(address))

    while True:
        # Ricezione dei dati in formato binario (8 byte per due interi)
        data = conn.recv(8)
        if not data:
            # Se non vengono ricevuti dati, esce dal ciclo
            break

        # Decodifica i dati ricevuti: due interi (x, y)
        x, y = struct.unpack('ii', data)
        print(f"Ricevuto dal client: x = {x}, y = {y}")

        # Passa le variabili x e y alla funzione moveball()
        move_ball_to(x, y)

        # Opzionalmente, invia una conferma al client
        conn.send(b"Variabili ricevute e funzione moveball() eseguita.")

    # Chiude la connessione
    conn.close()


if __name__ == '__main__':
    server_program()
