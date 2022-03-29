from tkinter import Tk, Button, RAISED

root = Tk()
labels = [['1', '2', '3'],
          ['4', '5', '6'],
          ['7', '8', '9'],
          ['*', '0', '#']]

for r in range(4):
    for c in range(3):

        def handler(x=labels[r][c]):
            print(x)

        button = Button(root,
                        relief=RAISED,
                        padx=10,
                        text=labels[r][c],
                        command=handler)

        button.grid(row=r, column=c)


root.mainloop()
