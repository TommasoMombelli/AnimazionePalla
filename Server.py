import socket
from tkinter import *
import threading
from generate_qrcode import qr_code
from receive_data import receive_data
from multiprocessing import Process
from Ball import Ball
from receive_data import receive_dimensions
import time

dim_ball = 40
def server_program():

    # funzione per chiudere la finestra tkinter quando la connessione sarà chiusa
    def close_window():
        root.destroy()
        root.quit()
        

    
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
        
        

        # Creazione della finestra principale di Tkinter
        root = Tk()
        ball = Ball(root, dim_ball)
        root.attributes('-topmost', True)
        root.update()
        root.attributes('-topmost', False)

        # larghezza e altezza dello schermo del pc 
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()

        # calcolo dei fattori di scala per adattare le dimensioni 
        kx, ky= receive_dimensions(conn, screen_width-dim_ball, screen_height-dim_ball)
        
        # apertura del thread per la ricezione dei dati
        receive_thread = threading.Thread(target=receive_data, args=(conn, ball, kx,ky,close_window))
        receive_thread.daemon = True  
        receive_thread.start()
        
        

        # loop che tiene aperta la finestra tkinter
        root.mainloop()

if __name__ == '__main__':
    server_program()







