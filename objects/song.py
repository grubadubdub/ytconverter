from pytube import YouTube
from PIL import Image
import urllib.request

class Song:
    """"Container for song metadata"""

    def __init__(self, url: str):
        self.url = url
        self.stream_query = YouTube(url)

        self.title = self.stream_query.title

        while (self.title == "YouTube"):
            self.stream_query = YouTube(url)
            self.title        = self.stream_query.title

        self.audio            = self.stream_query.streams.get_audio_only()
        self.length           = self.stream_query.length
        self.thumbnail_url    = self.stream_query.thumbnail_url
        self.default_filename = self.audio.default_filename

        # get_thumbnail_image()

    def download(self, *args, **kwargs):
        return self.audio.download(*args, **kwargs)

    # def get_thumbnail_image(self, term, client_id, secret):
        # spotify = spotifyAPI.SpotifyAPI(client_id, secret)
        # ret = spotify.search(term, "track")
        # spotify.search_tracks(ret)
        # img = Image.open(urllib.request.urlopen(self.thumbnail_url))

        # img = Image.open(urllib.request.urlopen(self.thumbnail_url))
        # img = tk.PhotoImage(img)


