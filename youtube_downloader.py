from doctest import master
from logging import root
from tkinter import *
import tkinter as tk
from turtle import width

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

#Creating menu button in Tkinter
# def menuButtonInTinker():
#     top = Tk()
#     mb = Menubutton( top, text = &quot;GfG&quot;)
#     mb.grid()
#     mb.menu = Menu ( mb, tearoff=0)
#     mb[&quot;menu&quot;] = mb.menu
#     cVar = IntVar()
#     aVar = IntVar()
#     mb.menu.add_checkbutton(label='Contact', variable=cVar)
#     mb.menu.add_checkbutton(label='About', variable=aVar)
#     mb.pack()
#     top.mainloop()

#Creating Menu in Tkinter
def menuInTinker():
    root = Tk()
    menu = Menu(root)
    root.config(menu=menu)
    filemenu = Menu(menu)
    menu.add_cascade(label='File', menu=filemenu)
    filemenu.add_command(label='New')
    filemenu.add_command(label='Open...')
    filemenu.add_separator()
    filemenu.add_command(label='Exit', command=root.quit)
    helpmenu = Menu(menu)
    menu.add_cascade(label='Help', menu=helpmenu)
    helpmenu.add_command(label='About')
    mainloop()

#Creating Message in Tkinter
def messageinTinker():
    main = Tk()
    ourMessage = 'This is our Message'
    messageVar = Message(main, text=ourMessage)
    messageVar.config(bg='lightgreen')
    messageVar.pack()
    main.mainloop()

#Creating Radiobutton in Tkinter
def radioButtonInTkinter():
    root = Tk()
    v = IntVar()
    Radiobutton(root, text='GFG', variable=v, value=1).pack(anchor=W)
    Radiobutton(root, text='MIT', variable=v, value=2).pack(anchor=W)
    mainloop()

#Creating Scale in Tkinter
def scaleInTkinter():
    master = Tk()
    w = Scale(master, from_=0, to=42)
    w.pack()
    w = Scale(master, from_=0, to=200, orient=HORIZONTAL)
    w.pack()
    mainloop()

#Creating a Scrollbar in Tkinter
def scrollBarInTkinter():
    root = Tk()
    scrollbar = Scrollbar(root)
    scrollbar.pack(side=RIGHT, fill=Y)
    mylist = Listbox(root, yscrollcommand=scrollbar.set)
    for line in range(100):
        mylist.insert(END, 'This is line number' + str(line))
    mylist.pack( side = LEFT, fill = BOTH)
    scrollbar.config( command = mylist.yview)
    mainloop()

#Creating Text in Tkinter
def textInTkinter():
    root = Tk()
    T = Text(root, height=2, width=30)
    T.pack()
    T.insert(END, 'GeekforGeeks\nBEST WEBSITE\n')
    mainloop()

#Creating Toplevel in Tkinter
def toplevelInTkinter():
    root = Tk()
    root.title('GFG')
    top = Toplevel()
    top.title('Python')
    top.mainloop()

#Creating Spinbox in Tkinter
def spinboxInTkinter():
    master = Tk()
    w = Spinbox(master, from_=0, to = 10)
    w.pack()
    mainloop()

#Creating panned Window in tkinter
def pannedwindowInTkinter():
    m1 = PanedWindow()
    m1.pack(fill = BOTH, expand = 1)
    left = Entry(m1, bd = 5)
    m1.add(left)
    m2 = PanedWindow(m1, orient = VERTICAL)
    m1.add(m2)
    top = Scale( m2, orient = HORIZONTAL)
    m2.add(top)
    mainloop()


frame = Tk()
frame.geometry('400x200')
frame.title('Youtube downloader')
geek = Label(frame, text='Youtube downloader', font=('calibre', '25', 'bold'))
geek.grid(row=0, columnspan=1)


frame.mainloop()










