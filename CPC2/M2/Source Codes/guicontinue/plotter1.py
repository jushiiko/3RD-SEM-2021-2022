from tkinter import Tk, Canvas, Frame, Button, SUNKEN, LEFT, RIGHT


# function move() is called regardless of which button is pressed
def move(dx, dy):
    'move pen by dx horizontally and dy vertically'
    global x, y, canvas                  # x or y is modified
    canvas.create_line(x, y, x+dx, y+dy)
    x += dx
    y += dy


root = Tk()

# canvas with border of size 100 x 150
canvas = Canvas(root, height=100, width=150,
                relief=SUNKEN, borderwidth=3)
canvas.pack(side=LEFT)

# frame to hold the 4 buttons
box = Frame(root)
box.pack(side=RIGHT)

# the event handler cmd() is defined for each button
def cmd(): move(0, -10)
button = Button(box, text='up', command=cmd)
button.grid(row=0, column=0, columnspan=2)

def cmd(): move(-10, 0)
button = Button(box, text='left',command=cmd)
button.grid(row=1, column=0)

def cmd(): move(10, 0)
button = Button(box, text='right', command=cmd)
button.grid(row=1, column=1)

def cmd(): move(0, 10)
button = Button(box, text='down', command=cmd)
button.grid(row=2, column=0, columnspan=2)

# pen position, initially in the middle of the canvas
x, y = 50, 75

root.mainloop()

