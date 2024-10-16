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
    # get the hostname
    host = socket.gethostname()
    port = 5000  # initiate port no above 1024
    server_socket = socket.socket()  # get instance
    server_socket.bind((host, port))  # bind host address and port together

    qr_process = Process(target=qr_code)
    qr_process.start()

    # configure how many client the server can listen simultaneously
    server_socket.listen(1)
    conn, address = server_socket.accept()  # accept new connection
    print("Connection from: " + str(address))
    
    qr_process.terminate()
    qr_process.join()
    

    # Create the canvas and ball
    root = Tk()
    ball = Ball(root, dim_ball)
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    kx, ky= receive_dimensions(conn, screen_width-dim_ball, screen_height-dim_ball)

    # Start the thread to receive data from the client
    receive_thread = threading.Thread(target=receive_data, args=(conn, ball, kx,ky))
    receive_thread.daemon = True  # ensure the thread closes when the main window closes
    receive_thread.start()

    # Start the Tkinter main loop
    root.mainloop()


if __name__ == '__main__':
    server_program()
