import eyed3
import logging
import os
import pydub
from objects.song import Song
from PIL import Image, ImageTk
import utils.spotifyAPI as spotifyAPI

######## SETUP ########
logging.basicConfig(level=logging.DEBUG)

try:
    # Python2
    import Tkinter as tk
    from Tkinter import ttk
    from urllib2 import urlopen
except ImportError:
    # Python3
    import tkinter as tk
    from tkinter import ttk
    from urllib.request import urlopen

######## GUI ########
class GUI(object):
    # GLOBAL
    HEIGHT = 600
    WIDTH = 800
    images = []
    song = None
    label = None
    photo_frame = None
    entry = None
    meta_infos = [] # current song info shown in sidebar textboxes
    root = None
    tree = None

    # https://www.youtube.com/watch?v=HlN2BXNJzxA
    # https://www.youtube.com/watch?v=xQJeiEvNaAo
    # https://www.youtube.com/watch?v=6tzRAjLAtvU
    # https://www.youtube.com/watch?v=rcEyUNeZqmY

    def __init__(self, client_id, secret):
        super().__init__()
        self.client_id = client_id
        self.secret = secret

    def setup(self):
        self.root = tk.Tk()
        root = self.root
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

    def set_album_image(self, source):
        # TODO: fix frame size
        """
        Change the image displayed for a track given a source.
        """
        photo_frame = self.photo_frame

        if type(source) is Song:
            img = urlopen(source.thumbnail_url)
        else:
            img = urlopen(source)

        self.images = [img]
        img = Image.open(img)
        img = img.resize((200, 200), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(img)

        photo_frame.configure(image=photo)
        photo_frame.image = photo


    def download_audio(self, audio):
        # TODO: handle existing files (add counters?), filenames with emojis
        try:
            self.write_file(audio)
        except:
            logging.info("Meta info not filled")
            audio = self.get_yt_info(self.entry.get())
            self.write_file(audio)


    def write_file(self, audio):
        song_dir = os.getcwd() + f"\downloaded\\"
        oldname = song_dir + audio.default_filename
        newname = song_dir + self.meta_infos[0].get() + ".mp3"
        logging.info(f"Renaming file from {oldname.replace(song_dir, '')} to {newname.replace(song_dir, '')}")

        if os.path.isfile(newname):
            self.label["text"] = "File with this name already exists!"
        else:
            audio.download(output_path=song_dir)
            os.rename(oldname, newname)

        # convert MIME type to MP3 so we can use eyed3
        logging.info("Converting to MP3")
        mime_mp4 = pydub.AudioSegment.from_file(newname, "mp4")
        mime_mp4.export(newname, format="mp3")
        self.set_audio_tags(newname)

    def set_audio_tags(self, song_path):
        title, artist, album, release_date, track_no = [info.get() for info in self.meta_infos]
        audio = eyed3.load(song_path)
        audio.initTag()
        audio.tag.title = title
        audio.tag.artist = artist
        audio.tag.album = album
        audio.tag.track_num = track_no

        # cover art, will show in iTunes 
        img_res = urlopen(self.images[0].url)
        img_data = img_res.read()
        audio.tag.images.set(3, img_data, "image/jpeg", u"Cover art")

        audio.tag.save()
        logging.info(
            f"""Saving metadata for track:
        Title: {title}
        Artist: {artist}
        Album: {album}
        Track no.: {track_no}""")

    def get_yt_info(self, url):
        self.song = Song(url)
        self.label["text"] = self.song.title

        title = self.meta_infos[0]
        title.delete(0, tk.END)
        title.insert(0, self.song.title)

        self.set_album_image(self.song)
        return self.song

    def search_spotify(self):
        # if self.song is not None:
        spotify = spotifyAPI.SpotifyAPI(self.client_id, self.secret)
        term = self.meta_infos[0].get()
        try:
            ret = spotify.search(term, "track")
            results = spotify.search_tracks(ret)
            self.view_results(results)
        except ModuleNotFoundError:
            logging.error("Track not found -- try cutting down your search terms!")

    def view_results(self, results):
        """
        Show Spotify search results in TK
        :results list:
            Spotify search results 
        """
        # https://blog.tecladocode.com/tkinter-scrollable-frames/
        popup = tk.Tk()
        container = ttk.Frame(popup)
        canvas = tk.Canvas(container)
        scrollbar = ttk.Scrollbar(container, orient="vertical", command=canvas.yview)
        scrollable_frame = ttk.Frame(canvas)

        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )

        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        self.build_results(results, scrollable_frame)

        container.pack(fill="both")
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        popup.mainloop()

    def build_results(self, results, main_frame):
        """
        Insert tracks found with search term into Treeview.
        :results
        :main_frame
        """
        tree = ttk.Treeview(main_frame, selectmode='browse')

        labels = ["Title", "Artist", "Album", "Release Date", "Track No."]
        tree["columns"] = labels[1:]
        for i in range(len(labels)):
            tree.heading("#"+str(i), text=labels[i])
            tree.column("#"+str(i), stretch="yes")

        for res in results:
            artists = "".join(res["artists"][i]["name"] + ", " for i in range(len(res["artists"])))
            artists = artists[:-2]
            tree.insert(
                "", 
                "end", 
                text = res["name"],
                values = (
                        artists,
                        res["album"]["name"],
                        res["album"]["release_date"],
                        res["track_number"],
                        res["album"]["images"][0]["url"]))

        tree.bind('<ButtonRelease-1>', lambda event, t=tree: self.select_item(event, t))
        tree.pack(fill="both")

    def select_item(self, event, tree):
        all_vals = tree.item(tree.selection())
        self.set_entries(all_vals)

    def set_entries(self, all_vals):
        vals = all_vals["values"]
        vals.insert(0, all_vals["text"])
        infos = self.meta_infos
        for info, i in zip(infos, range(len(infos))):
            info.delete(0, tk.END)
            info.insert(0, vals[i])
        self.set_album_image(vals[-1])

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
        in_queue = tk.Frame(main_frame, bg="yellow")
        in_queue.place(relx=0.05, rely=0.2, relwidth=0.6, height="350px")

        label = tk.Label(in_queue)
        label.pack(fill="both")
        self.label = label;
        return in_queue

    def set_gallery_bar(self, main_frame):
        photo_frame = tk.Label(main_frame, image=None, bg="grey")
        self.photo_frame = photo_frame
        photo_frame.place(height="150px", width="150px", anchor=tk.CENTER, relx=0.5, rely=0.25)

        return photo_frame

    def set_meta_info(self, main_frame):
        labels = ["Title", "Artist", "Album", "Year", "Track No."]
        for i in range(len(labels)):
            label = tk.Label(main_frame, text=labels[i])
            label.pack(fill="x")

            meta_info = tk.Entry(main_frame)
            meta_info.pack(fill="x")
            self.meta_infos.append(meta_info)

        info_button = tk.Button(main_frame, text="Search Spotify", command=self.search_spotify)
        info_button.pack(pady="20px", fill="x")

        return meta_info

    def set_sidebar(self, main_frame):
        song_sidebar = tk.Frame(main_frame)
        song_sidebar.place(relx=0.67, relwidth=0.28, relheight=1.0)

        photo_frame = self.set_gallery_bar(song_sidebar)
        info_frame = tk.Frame(song_sidebar)
        info_frame.place(relwidth=1.0, relheight=0.8, rely=0.45)
        self.set_meta_info(info_frame)

        return song_sidebar