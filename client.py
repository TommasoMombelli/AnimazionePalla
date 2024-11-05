# import socket
# import json
# import tkinter as tk




# def client_program():
#     host = socket.gethostname()  # se sono sullo stesso PC
#     #host = "10.243.30.87"  #IP ILARIA
#     port = 5000  # socket server port number

#     client_socket = socket.socket()  # instantiate
#     client_socket.connect((host, port))  # connect to the server
#     # Get the screen dimensions
#     root = tk.Tk()
#     screen_width = root.winfo_screenwidth()
#     screen_height = root.winfo_screenheight()
    
#     # Send screen dimensions to the server
#     screen_dimensions = {"x": screen_width, "y": screen_height}
#     client_socket.send(json.dumps(screen_dimensions).encode())
#     # root.destroy()

#     while True:
#         # if message.lower().strip() != 'bye':
         
#          x = int(input("Inserisci la coordinata X: "))
#          y = int(input("Inserisci la coordinata Y: "))
        
#          # Create a dictionary with the coordinates
#          coordinates = {"x": x, "y": y}
    
#          # Convert the dictionary to a JSON string
#          message = json.dumps(coordinates)
#          client_socket.send(message.encode())  # send message
#     client_socket.close()  # close the connection


# if __name__ == '__main__':
#     client_program()



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
    screen_dimensions = {"x": 1536, "y": 864}
    client_socket.send(json.dumps(screen_dimensions).encode())

    try:
        while True:
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
            except ValueError:
                print("Invalid input. Please enter coordinates as 'x,y'.")

    finally:
        client_socket.close()  # close the connection

if __name__ == '__main__':
    client_program()