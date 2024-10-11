import socket
from tkinter import *
import threading
from basic_qrcode import qr_code
from multiprocessing import Process

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
    root.title("Ball Animation")

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    canvas = Canvas(root, height=screen_height, width=screen_width)
    canvas.pack()

    # Create the ball
    ball = canvas.create_oval(10, 10, 50, 50, fill="blue")
    canvas.moveto(ball, 100, 100)

    def receive_data():
        """Function to receive data from the client in a separate thread."""
        while True:
            try:
                # receive data stream. it won't accept data packet greater than 1024 bytes
                data = conn.recv(1024).decode()

                if not data:
                    # if data is not received break
                    break

                print("from connected user: " + str(data))

                # process the received data
                try:
                    data = data.strip("()")  # remove parentheses
                    x, y = data.split(",")   # split string by comma
                    x = float(x)  # convert x to integer
                    y = float(y)  # convert y to integer

                except ValueError:
                    print("Errore: formato delle coordinate non valido")
                    continue

                # Move the ball on the canvas (use `after` to ensure thread safety)
                canvas.after(0, canvas.moveto, ball, x, y)

            except Exception as e:
                print(f"Errore durante la ricezione dei dati: {e}")
                break

        conn.close()  # close the connection

    # Start the thread to receive data from the client
    receive_thread = threading.Thread(target=receive_data)
    receive_thread.daemon = True  # ensure the thread closes when the main window closes
    receive_thread.start()

    # Start the Tkinter main loop
    root.mainloop()


if __name__ == '__main__':
    server_program()
