from tkinter import Tk, Button, Frame, Label, Entry, END
from tkinter.messagebox import showinfo
from time import strptime, strftime, localtime

class ClickIt(Frame):


    def __init__(self, master=None):
        'constructor'
        Frame.__init__(self, master)
        self.pack()
        button = Button(self, text='Click it', command=self.clicked)
        button.pack()

    def clicked(self):

        time = strftime('Day:  %d %b %Y\nTime: %H:%M:%S %p\n', localtime())
        showinfo(message=time)

root =Tk()
clickit = ClickIt(root)
clickit.pack()
root.mainloop()
"""class Day(Frame):


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
        self.dateEnt.delete(0, END) """

