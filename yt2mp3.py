#!/usr/bin/env python3
# import spotifysearch
# import requests

import os
from pytube import YouTube as yt
import io
import base64
try:
    # Python2
    import Tkinter as tk
    from urllib2 import urlopen
except ImportError:
    # Python3
    import tkinter as tk
    from urllib.request import urlopen

HEIGHT = 600
WIDTH = 800

def get_album_image(url):
    global audio_file
    audio_file
    image_byt = urlopen(url).read()
    image_b64 = base64.encodestring(image_byt)
    photo = tk.PhotoImage(data=image_b64)

def download_audio(audio):
    # TODO: handle existing file
    try:
        oldname = audio.default_filename
        newname = oldname.replace("mp4", "mp3")

        audio.download()
        os.rename(oldname, newname)
    except:
        global audio_file
        audio_file = get_yt_info(entry.get())

        oldname = audio.default_filename
        newname = oldname.replace("mp4", "mp3")

        audio.download()
        os.rename(oldname, newname)


def get_yt_info(url):
    global audio_file
    audio_file = yt(url).streams

    audio = audio_file.get_audio_only()
    while (audio.title == "YouTube"):
        audio = audio_file.get_audio_only()

    label["text"] = audio.title
    return audio

def make_entry(main_frame):
    url_box = tk.Entry(main_frame)
    url_box.place(rely=0.1, relwidth=1.0, relheight=0.25)
    return url_box

def set_input_box(main_frame):
    global audio_file
    audio_file = None
    input_box = tk.Frame(main_frame)
    input_box.place(relx=0.05, rely=0.05, relwidth=0.6, relheight=0.2)

    get_button = tk.Button(input_box, text="Get", command=lambda: get_yt_info(entry.get()))
    get_button.place(rely=0.45, relwidth=0.2, relheight=0.25)


    download_button = tk.Button(input_box, text="Download", command=lambda: download_audio(audio_file))
    download_button.place(relx= 0.25, rely=0.45, relwidth=0.2, relheight=0.25)
    return input_box

def set_queue(main_frame):
    in_queue = tk.Frame(main_frame)
    in_queue.place(relx=0.05, rely=0.3, relwidth=0.6, relheight=0.65)
    global label
    label = tk.Label(in_queue)
    label.pack(fill="both")

def set_sidebar(main_frame):
    song_sidebar = tk.Frame(main_frame)
    song_sidebar.place(relx=0.67, rely=0.05, relwidth=0.28, relheight=0.9)




root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

main_frame = tk.Frame(root)
main_frame.place(anchor="c", relwidth=0.9, relheight=0.9, relx=0.5, rely=0.5)

input_box = set_input_box(main_frame)
entry = make_entry(input_box)

set_queue(main_frame)
set_sidebar(main_frame)

root.mainloop()


# # spotifysearch.search(title)