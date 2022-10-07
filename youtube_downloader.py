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
    SAVE_PATH = "../MINI_PROJECTS_PYTHON"
    link = "https://www.youtube.com/watch?v=czCFyzTVDR8"
    yt = YouTube(link)
    try:
        yt = YouTube(link)
    except:
        print('connection error')

    mp4files = yt.filter('mp4')
    yt.set_filename('Tkinter Youtube downloaded video')
    d_video = yt.get(mp4files[-1].extension, mp4files[-1].resolution)
    try:
        d_video.download(SAVE_PATH)
    except:
        print('some error')
    print('Task Completed')

submit_button = Button(root, text='download', command=download)
submit_button.grid(row=2, column=1)


root.mainloop()