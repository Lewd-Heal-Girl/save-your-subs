import threading
from queue import Queue
import requests
from pathlib import Path
import logging
from urllib.parse import urlparse

from ..utils import HaveSomeRestComrade, DownloadRequest, url_is_image
from ..reddit import ImgurMedia


LOGGER = logging.getLogger("imgur")

"""
find the client id in this java script file:
https://s.imgur.com/desktop-assets/js/main.bbbc7a722b2bd27c7035.js

it is near to a string which is as follows:
`l=window.location.hostname,d="localhost"===l?"imgur.com"`

and is a value of "y" 
`3e0",y="546c25a59c58ad7",b="6Ldqe`

it matches the regex: `(?<=",y=").*?(?=",b=")`
"""

# client id
# 546c25a59c58ad7

CLIENT_ID = "546c25a59c58ad7"
API_ENDPOINT = "https://api.imgur.com/post/v1/albums/{imgur_id}?include=media&client_id={client_id}"
COMRAD_COUNT = 3


class ImgurComrade(threading.Thread):
    def __init__(self, work_queue: Queue):
        self.work_queue = work_queue

        self.api_session = requests.Session()
        self.api_session.headers = {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/112.0",
            "Referer": "https://imgur.com/",
            "Origin": "https://imgur.com",
            "Connection": "keep-alive"
        }

        self.image_session = requests.Session()
        self.image_session.headers = {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/112.0",
            "Referer": "https://imgur.com/",
            "Connection": "keep-alive"
        }

        threading.Thread.__init__(self)

    def download_single(self, url: str, folder: Path, n: int, id_: str):
        img_format = url.split(".")[-1].split("?")[0]
        new_path = Path(folder, f"{str(n).zfill(2)}.{img_format}")

        if new_path.is_file():
            print(f"{new_path} already exists")
            return

        try:
            r = self.image_session.get(url)
            if r.status_code != 200:
                LOGGER.warning(f"{id_}: {url} returned {r.status_code}")

        except requests.RequestException:
            LOGGER.error(f"{id_}: Couldn't connect to imgur to direct download img {url}")
            return

        folder.mkdir(parents=True, exist_ok=True)

        print(url, "->", new_path)
        with new_path.open("wb") as f:
            f.write(r.content)

    def download_galerie(self, media_id: str, folder: Path, id_: str):
        media = []

        url = API_ENDPOINT.format(imgur_id=media_id, client_id=CLIENT_ID)

        try:
            r = self.api_session.get(url=url)

            media = r.json().get("media", list())
            if r.status_code == 404:
                return
            if r.status_code != 200:
                LOGGER.warning(f"{id_}: {url} responded with {r.status_code}")

        except requests.RequestException:
            LOGGER.error(f"{id_}: Couldn't connect to imgur api.")

        found_picture_in_gallery = False
        for i, image in enumerate(media):
            found_picture_in_gallery = True
            self.download_single(image.get("url"), folder, i, id_)
            
        if not found_picture_in_gallery:
            LOGGER.error(f"{id_}: didn't get any results for imgur gallery")

    def download(self, command: DownloadRequest):
        media_url = command.media.url

        if url_is_image(urlparse(media_url)):
            self.download_single(url=media_url, folder=command.folder, n=command.n, id_=command.id_)
        else:
            self.download_galerie(media_id=command.media.id, folder=command.folder, id_=command.id_)

    def run(self) -> None:
        command = self.work_queue.get()

        while command is not HaveSomeRestComrade:
            command = self.work_queue.get()
            if command is HaveSomeRestComrade:
                break

            command: DownloadRequest
            self.download(command=command)

        # gotta tell another worker to rest
        self.work_queue.put(HaveSomeRestComrade)


def spawn_imgur_comrades(comrad_count: int = COMRAD_COUNT) -> Queue:
    work_queue: Queue = Queue()

    for i in range(comrad_count):
        image_thread = ImgurComrade(work_queue=work_queue)
        image_thread.start()

    return work_queue
