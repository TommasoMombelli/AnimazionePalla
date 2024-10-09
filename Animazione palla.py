from tkinter import *
import time

#creazione canvas
root = Tk()
root.title("Ball Animation")

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

print("Larghezza della finestra:", screen_width)
print("Altezza della finestra:", screen_height)

x_max=screen_width
y_max=screen_height


pos_x = 100
pos_y = 100

canvas = Canvas(root, height= y_max, width= x_max)
canvas.pack()

# creazione palla
ball = canvas.create_oval(10, 10, 50, 50, fill="blue")

# movimento palla
canvas.moveto(ball, pos_x, pos_y)
canvas.update()

def move_ball_to(x_nuovo, y_nuovo):
    x, y = canvas.coords(ball)[:2]
    canvas.moveto(ball, x_nuovo, y_nuovo)
    canvas.update()
    time.sleep(0.01)
    x, y = canvas.coords(ball)[:2]


while True:
    move_ball_to()
    again = int(input("Vuoi muovere di nuovo la palla? (1 per sì, 0 per no): "))
    if again != 1:
        final_pos = canvas.coords(ball)
        break

root.mainloop()

