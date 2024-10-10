import socket


def client_program():
    host = socket.gethostname()  # se sono sullo stesso PC
    #host = "10.243.30.87"  #IP ILARIA
    port = 5000  # socket server port number

    client_socket = socket.socket()  # instantiate
    client_socket.connect((host, port))  # connect to the server

    # message = input(" ciao ")  # take input
    # il primo messagio devono essere le dimensioni della finestra del cellulare

    while True:
        # if message.lower().strip() != 'bye':
         
         x = int(input("Inserisci la coordinata X: "))
         y = int(input("Inserisci la coordinata Y: "))
        
         # formatta il messaggio come una coppia di coordinate
         message = f"({x}, {y})"
         # message = input(" -> ")  # again take input
         client_socket.send(message.encode())  # send message
    client_socket.close()  # close the connection


if __name__ == '__main__':
    client_program()