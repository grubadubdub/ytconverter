import secrets
import json, requests
from urllib.parse import urlencode
import base64
import datetime

class SpotifyAPI(object):

	"""
	Class for SpotifyAPI functions
	"""
	client_id = None
	client_secret = None
	access_token = None
	access_token_expires = datetime.datetime.now()
	access_token_expired = True
	token_url = "https://accounts.spotify.com/api/token"
	search_url = "https://api.spotify.com/v1/search"

	def __init__(self, client_id, client_secret, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.client_id = client_id
		self.client_secret = client_secret

	def get_client_creds(self):
		"""
		Returns base64 encoded string for authorization
		"""
		if self.client_id == None or self.client_secret == None:
			raise Exception("No client ID or secret found.")
		client_creds = f"{self.client_id}:{self.client_secret}"
		client_creds64 = base64.b64encode(client_creds.encode());
		return client_creds64.decode()

	def get_token_headers(self):
		"""
		Returns authorization header
		"""
		token_creds = self.get_client_creds()
		token_headers = {
				"Authorization": f"Basic {token_creds}"
			}
		return token_headers

	def get_token_data(self):
		"""
		Returns authorization parameter 'grant_type'
		"""
		token_data = {
			"grant_type": "client_credentials"
			}
		return token_data

	def get_access_token(self):
		"""
		Performs authorization with given client ID and secret. Returns the response access token.
		"""
		if self.perform_auth():
			return self.access_token

	def handle_data(self, data):
		access_token = data['access_token']
		expires_in = data['expires_in']
		now = datetime.datetime.now()
		expires = now + datetime.timedelta(seconds=expires_in)

		self.access_token = access_token
		self.access_token_expires = expires
		self.access_token_expired = now > expires

	def perform_auth(self):
		r = requests.post(
			self.token_url,
			data=self.get_token_data(),
			headers=self.get_token_headers()
		)
		if r.status_code not in range(200, 299):
			return False
		self.handle_data(r.json())
		return True

	def search(self, query, type, market="", limit=20, offset=0, include_external=""):
		"""
		Search for an item with a given query
		"""
		access_token = self.get_access_token()
		headers = {
			"Authorization": f"Bearer {access_token}"
		}

		# market = kwargs.get("market", None)
		# limit = kwargs.get("limit", None)
		# offset = kwargs.get("offset", None)
		# include_external = kwargs.get("include_external", None)

		data = urlencode({
			"q": query,
			"type": type
		})
		search_url = f"{self.search_url}?{data}"

		r = requests.get(
			search_url,
			headers=headers
		)

		return r.json()

spotify = SpotifyAPI(secrets.client_id, secrets.secret)
ret = spotify.search("exid hot pink", "track")
print(ret)
