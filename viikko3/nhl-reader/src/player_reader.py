import requests
import datetime

class PlayerReader:
    def __init__(self, url):
        self.response = requests.get(url).json()
        self.ct = datetime.datetime.now()
