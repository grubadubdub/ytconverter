from pytube import YouTube
from PIL import Image
import urllib.request

class Song:
    """"Container for song metadata"""

    def __init__(self, url: str):
        self.url = url
        self.stream_query = YouTube(url)

        self.title =         self.stream_query.title

        while (self.title == "YouTube"):
            self.stream_query = YouTube(url)
            self.title = self.stream_query.title

        self.audio =         self.stream_query.streams.get_audio_only()
        self.length =        self.stream_query.length
        self.thumbnail_url = self.stream_query.thumbnail_url
        self.default_filename = self.audio.default_filename

        # get_thumbnail_image()


    def get_thumbnail_image(self):
        img = Image.open(urllib.request.urlopen(self.thumbnail_url))
        # img = tk.PhotoImage(img)


