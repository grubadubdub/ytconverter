import eyed3
import logging
import os
from pydub import AudioSegment


# logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)

# mp4_version = AudioSegment.from_file("downloaded/Better.mp3", "mp4")
# mp4_version.export("downloaded/Better.mp3", format="mp3")

audio = eyed3.load("downloaded/Better.mp3")
audio.initTag()
audio.tag.artist = "Taeyeon"
audio.tag.save()
logging.info(audio)
