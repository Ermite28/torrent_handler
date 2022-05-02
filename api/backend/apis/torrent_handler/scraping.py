
from main import settings
import requests


class Scrapper():
    def __init__(self, site='yts', limit=2):
        self.site = site
        self.limit = limit 
    
    def get_torrents(self, name):
        torrents = requests.request(
            "GET", settings.TORRENT_SCRAPPER_URL + f"/api/v1/search?site={self.site}&query={name}&limit={self.limit}"
        ).json()
        if "error" in torrents:
            raise Exception("No found")
        return torrents
    
    def get_score(self, model, torrent):
        if model == torrent :
            return 1
        else:
            return 0
    
    

