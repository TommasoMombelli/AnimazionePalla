import socket
import json


def client_program():
    host = socket.gethostname()  # se sono sullo stesso PC
    #host = "10.243.30.87"  #IP ILARIA
    port = 5000  # socket server port number

    client_socket = socket.socket()  # instantiate
    client_socket.connect((host, port))  # connect to the server


    while True:
        # if message.lower().strip() != 'bye':
         
         x = int(input("Inserisci la coordinata X: "))
         y = int(input("Inserisci la coordinata Y: "))
        
         # Create a dictionary with the coordinates
         coordinates = {"x": x, "y": y}
    
         # Convert the dictionary to a JSON string
         message = json.dumps(coordinates)
         client_socket.send(message.encode())  # send message
    client_socket.close()  # close the connection


if __name__ == '__main__':
    client_program()