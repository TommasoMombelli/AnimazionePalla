import json
from Ball import Ball
from math import floor
from tkinter import *
import time 


def receive_data(conn, ball: Ball, kx, ky,screen_width, screen_height):
    
    delta=5
    data_splitted = []
    
    x_c = screen_width/2
    y_c = screen_height/2
    
    while ball.running:   
        try:
            # recezione dei dati, di dimensione massima 8000 byte, dal client
            data = conn.recv(8000).decode()
            
            #separazione delle coordinate in base al carattere ";" e rimozione degli elementi vuoti
            data_splitted=data.split(";")
            if '' in data_splitted:
                data_splitted.remove('')

            for data in data_splitted:
                # chiusura della connessione quando arriva la stringa "close"
                
                if data == 'close': 
                    print("Connessione chiusa perchè ricevuto 'close'")  
                    ball.close()
                    break
                try:
                    # conversione delle coordinate in un Json
                    coordinates = json.loads(data)
                    x = coordinates['x']
                    y = coordinates['y']
                    print(f"X={x}, Y={y}")
                    
                    # controllo se le coordinate ricevute sono vicine al centro della schermata
                    if x*kx > x_c-delta and x*kx < x_c+delta and y*ky > y_c-delta and y*ky < y_c+delta:
                        ball.update_coords(floor(x*kx), floor(y*ky))
                        print("Contact detected, closing connection")
                        conn.send("winner".encode())
                        ball.winner=True
                        time.sleep(3)
                        ball.close()
                        break       
                
                # gestione dell'eccezione in caso di formato delle coordinate non valido
                except ValueError:
                    print("Errore: formato delle coordinate non valido")
                    continue
                
                # spostamento della palla alle coordinate ricevute
                ball.update_coords(floor(x*kx), floor(y*ky))
        
        # gestione dell'eccezione in caso di errore durante la ricezione dei dati
        except Exception as e:
            if ball.is_running():
                break
            else:
                print(f"Errore durante la ricezione dei dati: {e}") 
                break
    # chiusura della connessione in caso non arrivino più dati
    if not ball.is_running():
        print("Connessione chiusa perchè non arrivano più dati")  

# recezione delle dimensioni dello schermo del client
def receive_dimensions(conn, screen_width, screen_height):
    data=conn.recv(8000).decode()
    dimensions=json.loads(data)
    if(dimensions['x'] == 0):
        x = 400
    else:
        x = dimensions['x']
    if(dimensions['y'] == 0):
        y = 800
    else:
        y = dimensions['y']
        
    print(f"Received dimensions: width={x}, height={y}")
    # calcolo dei fattori di scala per adattare le dimensioni dello schermo del
    # client (cellulare) a quelle del pc
    kx=screen_width/x
    ky=screen_height/y
    return kx,ky


    
    
   




        







