import socket
import threading

import tkinter

import customtkinter as ctk

from generate_qrcode import qr_code
from receive_data import receive_data, receive_dimensions
from multiprocessing import Process
from Ball import Ball
import pyautogui



r_ball = 20


def server_program():
    camera=False
      
    # definizione dell'host e della porta
    host = socket.gethostname()
    port = 5000 

    # Creazione del socket server e associazione all'host e alla porta
    server_socket = socket.socket()  
    server_socket.bind((host, port))  

    while True:
        # processo che genera il qr code
        qr_process = Process(target=qr_code) 
        server_socket.settimeout(60)
        qr_process.start()
        # attesa di una connessione
        try:
            # configurazione del numero massimo di connessioni in coda
            server_socket.listen(1)

            # accettazione di una nuova connessione
            conn, address = server_socket.accept()  
            print("Connection from: " + str(address))
        except socket.timeout:
            print("Connection timed out")
            qr_process.terminate()
            qr_process.join()
            break

        # terminazione del processo che genera il qr code doppo che la 
        # connessione è stata stabilita
        qr_process.terminate()
        qr_process.join()        

        # Da qua inizia il ciclo dei openCV
        screen_width, screen_height = pyautogui.size()
        
        #funzione per la creazione del popup per la scelta dello sfondo
        def ask_question():

            window = ctk.CTk()  
            window.title("Domanda")
            window.geometry("400x200")
            window.config(bg="#f5f5f5")
            

            def on_yes():
                print("Sì selezionato")
                result.set(True)
                window.destroy()

            def on_no():
                print("No selezionato")
                result.set(False)
                window.destroy()

            # Label
            label = ctk.CTkLabel(
                window, 
                text="Vuoi utilizzare il video \n della webcam come sfondo?", 
                fg_color= "#f5f5f5",
                text_color="#333333", 
                font=("Lora", 14)
            )
            label.pack(pady=30)

            # Frame per i pulsanti
            button_frame = ctk.CTkFrame(window ,fg_color="#f5f5f5", bg_color="white")
            button_frame.pack()

            #Caratteristiche pulsanti
            yes_button = ctk.CTkButton(
                button_frame, 
                text="Sì", 
                command=on_yes, 
                fg_color="#00bcdc", 
                text_color="#f5f5f5", 
                corner_radius=15,  
                width=100, 
                height=40, 
                font=("Lora", 12)
            )
            no_button = ctk.CTkButton(
                button_frame, 
                text="No", 
                command=on_no, 
                fg_color="#00bcdc", 
                text_color="#f5f5f5", 
                corner_radius=15,  
                width=100, 
                height=40, 
                font=("Lora", 12)
            )

            yes_button.pack(side="left", padx=10)
            no_button.pack(side="right", padx=10)

            # Variabile per memorizzare la scelta
            result = ctk.BooleanVar()
            window.mainloop()

            return result.get()

        
        camera = ask_question()
        conn.send("start".encode())
        

        ball = Ball(screen_width, screen_height)

        # calcolo dei fattori di scala per adattare le dimensioni 
        kx, ky= receive_dimensions(conn, screen_width-r_ball, screen_height-r_ball)
               
        # apertura del thread per la ricezione dei dati
        receive_thread = threading.Thread(target=receive_data, args=(conn, ball, kx,ky, screen_width, screen_height))
        receive_thread.daemon = True  
        receive_thread.start()
        
        ball.cv2Loop(camera)       
        
        

if __name__ == '__main__':
    server_program()







