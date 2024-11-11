
import json
from math import radians, cos, sin
from random import choice
from tkinter import *
from tkinter import messagebox

def receive_data(conn, ball, kx, ky, close_window):
        closed=False
        data_splitted = []
        x_c = ball.screen_width/2-ball.dim_ball/2
        y_c = ball.screen_height/2-ball.dim_ball/2
        delta = 5
        print(f"X_c={x_c}, Y_c={y_c}")
        while True:
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
                        closed=True
                        print("Connessione chiusa perchè ricevuto 'close'")  
                        close_window()
                        break
                    try:
                        # conversione delle coordinate in un Json
                        coordinates = json.loads(data)
                        x = coordinates['x']
                        y = coordinates['y']
                        print(f"X={x}, Y={y}")
                        
                        if x*kx > x_c-delta and x*kx < x_c+delta and y*ky > y_c-delta and y*ky < y_c+delta:
                            ball.move_ball(x*kx,y*ky)
                            print("Contact detected, closing connection")
                            conn.send("winner".encode())
                            # messagebox.showinfo("Vittoria", "Hai vinto!")
                            testo_vittoria(ball, closed)
                            closed  = True
                            close_window()
                            break       
                    
                    # gestione dell'eccezione in caso di formato delle coordinate non valido
                    except ValueError:
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
        if not closed:
           print("Connessione chiusa perchè non arrivano più dati")  
           close_window()


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

# testo che fa lo zoom 
def testo_vittoria(ball, closed):
    
    def pulsate_text():
        current_color = ball.canvas.itemcget(text_id, "fill")
        next_color = "red" if current_color == "blue" else "blue"
        ball.canvas.itemconfig(text_id, fill=next_color)
        if not closed:
            ball.canvas.after(500, pulsate_text)

    def zoom_text(font_size=36, delta=1):
        nonlocal text_id
        # Cambia la dimensione del font per dare un effetto zoom
        ball.canvas.itemconfig(text_id, font=("Helvetica", int(font_size), "bold"))
        new_size = font_size + delta
        # Imposta un intervallo di oscillazione tra 36 e 50
        if new_size > 50 or new_size < 36:
            delta = -delta  # Inverte la direzione dello zoom
        if not closed:
            ball.canvas.after(100, zoom_text, new_size, delta)
            
    def create_firework(x, y, colors=("red", "yellow", "blue", "green", "purple")):
        particles = []
        for _ in range(20):
            angle = radians(choice(range(360)))
            speed = choice(range(5, 15))
            dx = cos(angle) * speed
            dy = sin(angle) * speed
            color = choice(colors)
            particle = ball.canvas.create_oval(x, y, x+5, y+5, fill=color, outline=color)
            particles.append((particle, dx, dy))
        return particles

    def animate_firework(particles, steps=20):
        for _ in range(steps):
            for particle, dx, dy in particles:
                ball.canvas.move(particle, dx, dy)
            ball.canvas.update()
            ball.canvas.after(50)
        for particle, _, _ in particles:
            ball.canvas.delete(particle)

    def show_fireworks():
        for _ in range(2):
            x = ball.screen_width / 2
            y = ball.screen_height / 2 - 200
            particles = create_firework(x, y)
            animate_firework(particles)
        if not closed:
            ball.canvas.after(1000, show_fireworks)

    # Crea il testo iniziale
    text_id = ball.canvas.create_text(ball.screen_width/2, ball.screen_height/2-200, text="Hai vinto!!", font=("Helvetica", 36, "bold"), fill="red")
    
    # Avvia le animazioni
    #pulsate_text()    
    zoom_text()
    show_fireworks()
    
    
   




        







