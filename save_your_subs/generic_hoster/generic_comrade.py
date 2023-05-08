import threading
from queue import Queue
import requests
from pathlib import Path
import logging

from ..utils import HaveSomeRestComrade, DownloadRequest


LOGGER = logging.getLogger("generic")

COMRAD_COUNT = 7


class GenericComrade(threading.Thread):
    def __init__(self, work_queue: Queue):
        self.work_queue = work_queue

        self.image_session = requests.Session()
        self.image_session.headers = {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/112.0",
            "Referer": "https://www.reddit.com/",
            "Connection": "keep-alive"
        }

        threading.Thread.__init__(self)

    def download(self, command: DownloadRequest):
        folder = command.folder
        url = command.media.url
        n = command.n

        img_format = url.split(".", 1)[-1].split("?")[0]
        new_path = Path(folder, f"{str(n).zfill(2)}.{img_format}")

        if new_path.is_file():
            print(f"{new_path} already exists")
            return

        try:
            r = self.image_session.get(url)

            if r.status_code != 200:
                LOGGER.warning(f"{command.id_}: {url} responded with {r.status_code}")
        except requests.RequestException:
            LOGGER.error(f"{command.id_}: Couldn't connect to {url}")
            return

        folder.mkdir(parents=True, exist_ok=True)

        print(url, "->", new_path)
        with new_path.open("wb") as f:
            f.write(r.content)

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


def spawn_generic_comrades(comrad_count: int = COMRAD_COUNT) -> Queue:
    work_queue: Queue = Queue()

    for i in range(comrad_count):
        image_thread = GenericComrade(work_queue=work_queue)
        image_thread.start()

    return work_queue
