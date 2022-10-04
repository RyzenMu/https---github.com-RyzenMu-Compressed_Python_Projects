from tkinter import *
import tkinter as tk

# Hello World in Tkinter
def tkinter_HelloWorld():

    root = Tk() #Create the root (base) window

    w = Label(root, text="Hello World!!!") # Create a label with words

    w.pack() #Put the label into the window

    root.mainloop() # start the event loop



# Simple Application in Tkinter
def simpleTkinterApplication():
    class Application(tk.Frame):

        def __init__(self, master=None):
            tk.Frame.__init__(self, master)
            self.grid()
            self.createWidgets()

        def createWidgets(self):
            self.medialLbalel = tk.Label(self, text='Hello World!')
            self.medialLbalel.config(bg="#00ffff")
            self.medialLbalel.grid()
            self.quitButton = tk.Button(self, text='Quit', command=self.quit)
            self.quitButton.grid()

    app = Application()
    app.master.title('Sample application')
    app.mainloop()


# Simple Button in Tkinter

def buttonInTkinter():
    r= Tk()
    r.title('Counting Seconds')
    button = tk.Button(r, text='Stop', width=25, command=r.destroy)
    button.pack()
    r.mainloop()






