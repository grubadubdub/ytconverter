#!/usr/bin/env python3
# import spotifysearch
import requests
from io import BytesIO
import base64

import os
from pytube import YouTube as yt
from song import Song
from PIL import Image, ImageTk
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

# GLOBAL
images = []
song = None
label = None
photo_frame = None

# https://www.youtube.com/watch?v=HlN2BXNJzxA
# https://www.youtube.com/watch?v=xQJeiEvNaAo

def get_album_image():
    img = Image.open(urlopen(song.thumbnail_url))
    img = img.resize((500, 500), Image.ANTIALIAS)
    photo = ImageTk.PhotoImage(img)

    images.append(photo)

    global photo_frame
    photo_frame.configure(image=photo)
    photo_frame.image = photo


def download_audio(audio):
    # TODO: handle existing file, filenames with emojis
    try:
        write_file(audio)
    except:
        audio = get_yt_info(entry.get())
        write_file(audio)


def write_file(audio):
    song_dir = os.getcwd() + f"\downloaded\\"
    oldname = song_dir + audio.default_filename
    newname = oldname.replace("mp4", "mp3")

    song.audio.download(output_path=song_dir)
    os.rename(oldname, newname)


def get_yt_info(url):
    global song, label
    song = Song(url)
    label["text"] = song.title

    get_album_image()

def make_entry(main_frame):
    url_box = tk.Entry(main_frame)
    url_box.place(rely=0.1, relwidth=1.0, relheight=0.25)
    return url_box

def set_input_box(main_frame):
    input_box = tk.Frame(main_frame)
    input_box.place(relx=0.05, rely=0.05, relwidth=0.6, relheight=0.2)

    get_button = tk.Button(input_box, text="Get", command=lambda: get_yt_info(entry.get()))
    get_button.place(rely=0.45, relwidth=0.2, relheight=0.25)

    download_button = tk.Button(input_box, text="Download", command=lambda: download_audio(song))
    download_button.place(relx= 0.25, rely=0.45, relwidth=0.2, relheight=0.25)
    return input_box

def set_queue(main_frame):
    in_queue = tk.Frame(main_frame)
    in_queue.place(relx=0.05, rely=0.3, relwidth=0.6, relheight=0.65)
    global label
    label = tk.Label(in_queue)
    label.pack(fill="both")
    return in_queue

def set_sidebar(main_frame):
    song_sidebar = tk.Frame(main_frame, bg="green")
    song_sidebar.place(relx=0.67, relwidth=0.28, relheight=0.9)

    photo_canvas = tk.Canvas(song_sidebar, bg="red")
    global photo_frame
    photo_frame = tk.Label(photo_canvas, image=None)
    photo_frame.pack(fill="both")

    photo_canvas.place(relwidth=1.0, relheight=0.5)

    return song_sidebar


root = tk.Tk()
root.title("YTConverter")

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

main_frame = tk.Frame(root)
main_frame.place(anchor="c", relwidth=0.9, relheight=0.9, relx=0.5, rely=0.5)

input_box = set_input_box(main_frame)
entry = make_entry(input_box)

queue = set_queue(main_frame)
sidebar = set_sidebar(main_frame)

root.mainloop()


# # spotifysearch.search(title)
# ca1262827006440dbd4c0371af08d13e
# aa7da1e3afdd4f2cb416f1d730a75c64
# user: 31jbzyaxatd7q37tat6urb5xeuve