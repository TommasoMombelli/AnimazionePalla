import json
from tkinter import *

def receive_data(conn, ball, kx, ky):
        data2 = []
        """Function to receive data from the client in a separate thread."""
        while True:
            try:
                # receive data stream. it won't accept data packet greater than 1024 bytes
                data = conn.recv(8000).decode()

                if not data:
                    # if data is not received break
                    break
                
                data2=data.split(";")
                data2.remove('')
                # print("from connected user: " + str(data))

                

                # process the received data
                # while len(data2) > 0:
                #     data = data2.pop(0)
                for data in data2:
                    try:
                        coordinates = json.loads(data)
                        x = coordinates['x']
                        y = coordinates['y']
                        print(f"X={x}, Y={y}")

                    except ValueError:
                        print("Errore: formato delle coordinate non valido")
                        continue

                    ball.move_ball(x*kx,y*ky)

            except Exception as e:
                print(f"Errore durante la ricezione dei dati: {e}")
                break

        conn.close()  # close the connection


def receive_dimensions(conn, screen_width, screen_height):
    data=conn.recv(8000).decode()
    dimensions=json.loads(data)
    
    x = dimensions['x']
    y = dimensions['y']
    print(f"Received dimensions: width={x}, height={y}")
    kx=screen_width/x
    ky=screen_height/y
    return kx,ky


     
     