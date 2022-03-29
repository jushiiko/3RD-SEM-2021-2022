from tkinter import Tk, Button, Entry, Label, END, Frame
from time import strptime, strftime
from tkinter.messagebox import showinfo


class Day(Frame):


    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()

        # label
        label = Label(self, text='Enter date')
        label.grid(row=0, column=0)

        # entry
        self.dateEnt = Entry(self)  # instance variable
        self.dateEnt.grid(row=0, column=1)

        # button
        button = Button(self, text='Enter', command=self.compute)
        button.grid(row=1, column=0, columnspan=2)

    def compute(self):


        # read date from entry dateEnt
        date = self.dateEnt.get()

        # compute weekday corresponding to date
        weekday = strftime('%A', strptime(date, '%b %d, %Y'))

        # display the weekday in a pop-up window
        showinfo(message='{} was a {}'.format(date, weekday))

        # delete date from entry dateEnt
        self.dateEnt.delete(0, END)

root =Tk()
clickit = Day(root)
clickit.pack()
root.mainloop()