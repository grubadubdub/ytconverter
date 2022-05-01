import objects.gui
import utils.secrets as secrets

instance = objects.gui.GUI(secrets.client_id, secrets.secret)
instance.setup()