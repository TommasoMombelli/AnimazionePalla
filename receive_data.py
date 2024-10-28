import json
from tkinter import *

def receive_data(conn, ball, kx, ky, close_window):
        closed=False
        data_splitted = []
        while True:
            try:
                # recezione dei dati, di dimensione massima 8000 byte, dal client
                data = conn.recv(8000).decode()

                if not data:
                    close_window()
                    print("Connessione chiusa")
                    break
                
                #separazione delle coordinate in base al carattere ";" e rimozione degli elementi vuoti
                data_splitted=data.split(";")
                data_splitted.remove('')


                for data in data_splitted:
                    try:
                        # conversione delle coordinate in un Json
                        coordinates = json.loads(data)
                        x = coordinates['x']
                        y = coordinates['y']
                        print(f"X={x}, Y={y}")
                    
                    # gestione dell'eccezione in caso di formato delle coordinate non valido
                    # chiusura della connessione quando arriva la stringa "close"
                    except ValueError:
                        if data == "close":
                            close_window()
                            print("Connessione chiusa")
                            closed=True
                            break
                        print("Errore: formato delle coordinate non valido")
                        continue
                    
                    # spostamento della palla alle coordinate ricevute
                    ball.move_ball(x*kx,y*ky)
            
            # gestione dell'eccezione in caso di errore durante la ricezione dei dati
            except Exception as e:
                if closed:
                    break
                else:
                    print(f"Errore durante la ricezione dei dati: {e}")
                    break

        # chiusura della connessione in caso non arrivino più dati
        conn.close()
        close_window()
        print("Connessione chiusa")  
        


def receive_dimensions(conn, screen_width, screen_height):
    # recezione delle dimensioni dello schermo del client
    data=conn.recv(8000).decode()
    dimensions=json.loads(data)
    x = dimensions['x']
    y = dimensions['y']
    print(f"Received dimensions: width={x}, height={y}")
    
    # calcolo dei fattori di scala per adattare le dimensioni dello schermo del
    # client (cellulare) a quelle del pc
    kx=screen_width/x
    ky=screen_height/y
    return kx,ky

