from tkinter import *
from pytube import *

root = Tk()

root.title('Youtube Downloader')

label_main = Label(root, text='YOUTUBE DOWNLOADER')
label_main.grid(row=0, column=0, columnspan=2)

label_link = Label(root, text='Paste the Link')
label_link.grid(row=1, column=0)

string_inside_box = StringVar()



link_entry = Entry(root, width=30, textvariable=string_inside_box)
link_entry.grid(row=1, column=1)


def download():
   yt=YouTube(string_inside_box.get())
   videos_list = yt.streams.filter(progressive=True, file_extension='mp4')
   videos_list[-1].download()

submit_button = Button(root, text='download', command=download)
submit_button.grid(row=2, column=1)


root.mainloop()

# yt = YouTube('http://youtube.com/watch?v=9bZkp7q19f0')
# videos_list = yt.streams.filter(progressive=True, file_extension='mp4')
# videos_list[-1].download()