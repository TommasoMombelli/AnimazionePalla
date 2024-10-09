import socket


def client_program():
    host = "10.243.30.87"  #se non sono sullo stesso pc come host devo mettere l'ip del server (PC DI ILARIA = "10.243.30.87" )
    port = 5000  # socket server port number

    client_socket = socket.socket()  # instantiate
    client_socket.connect((host, port))  # connect to the server

    message = input(" -> ")  # take input

    while message.lower().strip() != 'bye': 
        client_socket.send(message.encode())  # send message
        # data = client_socket.recv(1024).decode()  # receive response

        # print('Received from server: ' + data)  # show in terminal

        message = input(" -> ")  # again take input

    client_socket.close()  # close the connection


if _name_ == '_main_':
    client_program()