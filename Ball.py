from tkinter import *

class Ball():
    def __init__(self, tk, dim_ball):
        root = tk
        root.title("Ball Animation")

        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()

        self.canvas = Canvas(root, height= screen_height, width= screen_width)
        self.canvas.pack()

        # creazione palla
        self.ball = self.canvas.create_oval(0, 0, dim_ball, dim_ball, fill="blue")

        # movimento palla
        self.canvas.moveto(self.ball, 100, 100)
        
    
    def move_ball(self, x, y):
        self.canvas.after(0, self.canvas.moveto, self.ball, x, y)