import yt2mp3
import secrets

instance = yt2mp3.GUI(secrets.client_id, secrets.secret)
instance.setup()