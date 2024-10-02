from tkinter import *
import time


def move_ball():
    x, y = 5, 5
    while True:
        canvas.move(ball, x, y)
        pos = canvas.coords(ball)
        if pos[2] >= canvas.winfo_width() or pos[0] <= 0:
            x = -x
        if pos[3] >= canvas.winfo_height() or pos[1] <= 0:
            y = -y
        canvas.update()
        time.sleep(0.01)


# creazione canvas
root = Tk()
root.title("Ball Animation")

canvas = Canvas(root, height=1000, width=1000)
canvas.pack()

# creazione palla
ball = canvas.create_oval(10, 10, 50, 50, fill="blue")

# movimento palla
canvas.move(ball, 100, 100)
canvas.update()

root.mainloop()
