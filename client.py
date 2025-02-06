import socket
import json
import tkinter as tk


def client_program():
    host = socket.gethostname()  # se sono sullo stesso PC
    #host = "10.243.30.87"  #IP ILARIA
    port = 5000  # socket server port number

    client_socket = socket.socket()  # instantiate
    client_socket.connect((host, port))  # connect to the server
       
    # Send screen dimensions to the server
    screen_dimensions = {"x": 1920, "y": 1080}
    client_socket.send(json.dumps(screen_dimensions).encode())

    try:
        while True:
            print("aaaa")
            # data = client_socket.recv(1024).decode()
            # print('Received from server: ' + data)
            # Get user input
            user_input = input("Enter coordinates as 'x,y' or type 'close' to end: ")

            if user_input.lower() == 'close':
                client_socket.send("close".encode())
                break

            try:
                x, y = map(int, user_input.split(','))
                coordinates = {'x': x, 'y': y}
                message = json.dumps(coordinates)
                client_socket.send(message.encode())  # send message
                
                # Check if the server has sent any data
                client_socket.settimeout(1.0)  # Set a timeout for receiving data
                try:                                                                            
                    data = client_socket.recv(1024).decode()
                    if data:
                        print("Received from server:", data)
                        if data == "winner":
                            print("You are the winner!")
                            break
                except socket.timeout:
                    pass  # No data received, continue with the loop
            except ValueError:
                print("Invalid input. Please enter coordinates as 'x,y'.")

    finally:
        client_socket.close()  # close the connection

if __name__ == '__main__':
    client_program()
    
    
    
    