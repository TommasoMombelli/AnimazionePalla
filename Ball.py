from tkinter import *
# Importazione del modulo Tkinter
class Ball():
    def __init__(self, tk, dim_ball):
        #Creazione di un'istanza di una finestra Tkinter e impostazione del suo titolo
        root = tk
        root.title("Ball Animation")
        
        #larghezza e altezza dello schermo
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()

        #Creazione di un Canvas all'interno della finestra su cui disegnare
        self.canvas = Canvas(root, height= screen_height, width= screen_width)
        self.canvas.pack()

        #Creazione di una palla rossa alla posizione (0,0) sul canvas
        self.ball = self.canvas.create_oval(0, 0, dim_ball, dim_ball, fill="red")

        #Spostamento della palla alla posizione (100,100) sul canvas
        self.canvas.moveto(self.ball, 100, 100)
        
    # Funzione per spostare la palla in una nuova posizione sul canvas, date in ingresso le coordinate x e y
    def move_ball(self, x, y):
        self.canvas.after(0, self.canvas.moveto, self.ball, x, y)