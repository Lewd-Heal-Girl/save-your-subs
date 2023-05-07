import threading
from queue import Queue
import requests
from pathlib import Path

from ..utils import HaveSomeRestComrade, DownloadRequest
from ..reddit import ImgurMedia

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
COMRAD_COUNT = 1


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

    def download_single(self, url: str, folder: Path, n: int):
        print(f"downloading: {url}")
        try:
            r = self.image_session.get(url)
            print(r.status_code)
        except requests.RequestException:
            return

        folder.mkdir(parents=True, exist_ok=True)

        img_format = url.split(".")[-1]
        new_path = Path(folder, f"{str(n).zfill(2)}.{img_format}")

        print("new path", new_path)
        with new_path.open("wb") as f:
            f.write(r.content)

    def download_galerie(self, media_id: str, folder: Path):
        media = []

        url = API_ENDPOINT.format(imgur_id=media_id, client_id=CLIENT_ID)

        # print(f"api call: {url}")
        try:
            r = self.api_session.get(url=url)
            # print(r.status_code)

            media = r.json().get("media", list())
            if r.status_code != 200:
                print(f"{url} responded with {r.status_code}")

        except requests.RequestException:
            print("Couldn't connect to imgur")

        for i, image in enumerate(media):
            self.download_single(image.get("url"), folder, i)

    def download(self, command: DownloadRequest):
        media_url = command.media.url

        url_frag = media_url.strip("/").split("/")[-1]
        if "." in url_frag:
            self.download_single(url=media_url, folder=command.folder, n=command.n)
        else:
            self.download_galerie(media_id=command.media.id, folder=command.folder)

    def run(self) -> None:
        command = self.work_queue.get()

        while command is not HaveSomeRestComrade:
            command = self.work_queue.get()
            if command is HaveSomeRestComrade:
                break

            command: DownloadRequest
            self.download(command=command)


def spawn_imgur_comrades(comrad_count: int = COMRAD_COUNT) -> Queue:
    work_queue: Queue = Queue()

    for i in range(comrad_count):
        image_thread = ImgurComrade(work_queue=work_queue)
        image_thread.start()

    return work_queue
