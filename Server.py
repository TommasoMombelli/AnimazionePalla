import socket
from tkinter import *
import threading
from generate_qrcode import qr_code
from receive_data import receive_data
from multiprocessing import Process
from Ball import Ball
from receive_data import receive_dimensions

dim_ball = 40

def server_program():
    # definizione dell'host e della porta
    host = socket.gethostname()
    port = 5000 

    # Creazione del socket server e associazione all'host e alla porta
    server_socket = socket.socket()  
    server_socket.bind((host, port))  

    # processo che genera il qr code
    qr_process = Process(target=qr_code)
    qr_process.start()

    # configurazione del numero massimo di connessioni in coda
    server_socket.listen(1)

    # accettazione di una nuova connessione
    conn, address = server_socket.accept()  
    print("Connection from: " + str(address))
    
    # terminazione del processo che genera il qr code doppo che la 
    # connessione è stata stabilita
    qr_process.terminate()
    qr_process.join()
    

    # Creazione dle canvas e della palla
    root = Tk()
    ball = Ball(root, dim_ball)

    # larghezza e altezza dello schermo del pc 
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # calcolo dei fattori di scala per adattare le dimensioni 
    kx, ky= receive_dimensions(conn, screen_width-dim_ball, screen_height-dim_ball)

    # funzione per chiudere la finestra tkinter quando la connessione sarà chiusa
    def close_window():
       root.destroy()
    
    # apertura del thread per la ricezione dei dati
    receive_thread = threading.Thread(target=receive_data, args=(conn, ball, kx,ky,close_window))
    receive_thread.daemon = True  
    receive_thread.start()


    # loop che tiene aperta la finestra tkinter
    root.mainloop()


if __name__ == '__main__':
    server_program()

