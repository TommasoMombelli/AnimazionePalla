from tkinter import *
import cv2 
from PIL import Image, ImageTk 
# Importazione del modulo Tkinter
class Ball():
    
    def __init__(self, tk, dim_ball):
            
        self.dim_ball = dim_ball
        #Creazione di un'istanza di una finestra Tkinter e impostazione del suo titolo
        root = tk
        root.title("Ball Animation")
        
        #larghezza e altezza dello schermo
        self.screen_width = root.winfo_screenwidth()
        self.screen_height = root.winfo_screenheight()
        
        

        #Creazione di un Canvas all'interno della finestra su cui disegnare
        self.canvas = Canvas(root, height= self.screen_height, width= self.screen_width)
        self.canvas.pack() 

        #creazione palla fissa
        self.fixedBall = self.canvas.create_oval(0, 0, dim_ball, dim_ball, fill="blue")
        #Creazione di una palla rossa alla posizione (0,0) sul canvas
        self.ball = self.canvas.create_oval(0, 0, dim_ball, dim_ball, fill="red")

        #Spostamento della palla alla posizione (100,100) sul canvas
        self.canvas.moveto(self.ball, 100, 100)
        #spostamento della palla fissa al centro dello schermo
        self.canvas.moveto(self.fixedBall, self.screen_width/2-dim_ball/2, self.screen_height/2-dim_ball/2)
        
    # Funzione per spostare la palla in una nuova posizione sul canvas, date in ingresso le coordinate x e y
    def move_ball(self, x, y):
        self.canvas.after(0, self.canvas.moveto, self.ball, x, y)


    
        