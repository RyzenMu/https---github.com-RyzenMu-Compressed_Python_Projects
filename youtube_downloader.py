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


# Create a line in canvas
def lineInTkinter():
    master = Tk()
    w = Canvas(master, width=40, height=60)
    w.pack()
    canvas_height = 20
    canvas_width = 200
    y = int(canvas_height / 2)
    w.create_line(0, y, canvas_width, y)
    w.mainloop()

# Create a check button in canvas
def checkButtonInTkinter():
    master = Tk()
    var1 = IntVar()
    Checkbutton(master, text='male', variable=var1).grid(row=0, sticky=W)
    var2 = IntVar()
    Checkbutton(master, text='female', variable=var2).grid(row=1, sticky=W)
    mainloop()

# Create a entry in the Tkinter
def entryInTkinter():
    master = Tk()
    Label(master, text='First Name').grid(row=0)
    Label(master, text='Last Name').grid(row=1)
    e1 = Entry(master)
    e2 = Entry(master)
    e1.grid(row=0, column=1)
    e2.grid(row=1, column=1)
    mainloop()

# Create a frame in Tkinter
def frameInTkinter():
    root = Tk()
    frame = Frame(root)
    frame.pack()
    bottomframe = Frame(root)
    bottomframe.pack( side = BOTTOM )
    redbutton = Button(frame, text='Red', fg='red')
    redbutton.pack( side = LEFT )
    greenbutton = Button(frame, text='Green', fg='green')
    greenbutton.pack( side = LEFT)
    bluebutton = Button(frame, text='Blue', fg='blue')
    bluebutton.pack( side = LEFT )
    blackbutton = Button(frame, text='Black', fg='black')
    blackbutton.pack( side = BOTTOM)
    root.mainloop()

#Label in Tkinter
def labelInTinker():
    root = Tk()
    w = Label(root, text='GeeksForGeeks.org')
    w.pack()
    root.mainloop()

#Listbox in Tkinter
def listboxInTinker():
    top = Tk()
    Lb = Listbox(top)
    Lb.insert(1, "Python")
    Lb.insert(2, 'Java')
    Lb.insert(3, 'C++')
    Lb.insert(4, 'Any other')
    Lb.pack()
    top.mainloop()

#menu button in Tkinter
def menuButtonInTinker():
    top = Tk()
    mb = Menubutton( top, text = &quot;GfG&quot;)
    mb.grid()
    mb.menu = Menu ( mb, tearoff=0)
    mb[&quot;menu&quot;] = mb.menu
    cVar = IntVar()
    aVar = IntVar()
    mb.menu.add_checkbutton(label='Contact', variable=cVar)
    mb.menu.add_checkbutton(label='About', variable=aVar)
    mb.pack()
    top.mainloop()






