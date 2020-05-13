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

class GUI(object):

    # GLOBAL
    HEIGHT = 600
    WIDTH = 800
    images = []
    song = None
    label = None
    photo_frame = None
    entry = None

    # https://www.youtube.com/watch?v=HlN2BXNJzxA
    # https://www.youtube.com/watch?v=xQJeiEvNaAo

    def __init__(self):
        super().__init__()

    def setup(self):
        root = tk.Tk()
        root.title("YTConverter")

        canvas = tk.Canvas(root, height=self.HEIGHT, width=self.WIDTH)
        canvas.pack()

        main_frame = tk.Frame(root)
        main_frame.place(anchor="c", relwidth=0.9, relheight=0.9, relx=0.5, rely=0.5)

        input_box = self.set_input_box(main_frame)
        self.entry = self.make_entry(input_box)

        queue = self.set_queue(main_frame)
        sidebar = self.set_sidebar(main_frame)

        root.mainloop()

    def get_album_image(self):
        song = self.song
        images = self.images
        photo_frame = self.photo_frame

        img = Image.open(urlopen(song.thumbnail_url))
        img = img.resize((500, 500), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(img)

        images.append(photo)

        photo_frame.configure(image=photo)
        photo_frame.image = photo


    def download_audio(self, audio):
        # TODO: handle existing file, filenames with emojis
        try:
            self.write_file(audio)
        except:
            audio = self.get_yt_info(self.entry.get())
            self.write_file(audio)


    def write_file(self, audio):

        song_dir = os.getcwd() + f"\downloaded\\"
        oldname = song_dir + audio.default_filename
        newname = oldname.replace("mp4", "mp3")

        if os.path.isfile(newname):
            self.label["text"] = "File with this name already exists!"
        else:
            audio.download(output_path=song_dir)
            os.rename(oldname, newname)


    def get_yt_info(self, url):
        self.song = Song(url)
        self.label["text"] = self.song.title

        self.get_album_image()
        return self.song

    def make_entry(self, main_frame):
        url_box = tk.Entry(main_frame)
        url_box.place(rely=0.1, relwidth=1.0, relheight=0.25)
        return url_box

    def set_input_box(self, main_frame):
        input_box = tk.Frame(main_frame)
        input_box.place(relx=0.05, rely=0.05, relwidth=0.6, relheight=0.2)

        get_button = tk.Button(input_box, text="Get", command=lambda: self.get_yt_info(self.entry.get()))
        get_button.place(rely=0.45, relwidth=0.2, relheight=0.25)

        download_button = tk.Button(input_box, text="Download", command=lambda: self.download_audio(self.song))
        download_button.place(relx= 0.25, rely=0.45, relwidth=0.2, relheight=0.25)
        return input_box

    def set_queue(self, main_frame):
        in_queue = tk.Frame(main_frame)
        in_queue.place(relx=0.05, rely=0.3, relwidth=0.6, relheight=0.65)
        label = tk.Label(in_queue)
        label.pack(fill="both")
        self.label = label;
        return in_queue

    def set_sidebar(self, main_frame):
        song_sidebar = tk.Frame(main_frame, bg="green")
        song_sidebar.place(relx=0.67, relwidth=0.28, relheight=0.9)

        photo_canvas = tk.Canvas(song_sidebar, bg="red")
        photo_frame = tk.Label(photo_canvas, image=None)
        photo_frame.pack(fill="both")
        self.photo_frame = photo_frame

        photo_canvas.place(relwidth=1.0, relheight=0.5)

        return song_sidebar


# # spotifysearch.search(title)
# ca1262827006440dbd4c0371af08d13e
# aa7da1e3afdd4f2cb416f1d730a75c64
# user: 31jbzyaxatd7q37tat6urb5xeuve