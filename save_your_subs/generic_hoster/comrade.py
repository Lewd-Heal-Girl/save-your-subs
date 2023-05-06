from queue import Queue
import requests

from .classes import DownloadRequest, HaveSomeRestComrade


def download(download_request: DownloadRequest, session: requests.Session):
    try:
        r = session.get(download_request.media.url)
        print(r.request.headers)
        print(r.headers)
        print(download_request.media.url)
        print(r.status_code)
    except requests.RequestException:
        print("Comrade failed")
        return

    with download_request.folder.open("wb") as f:
        f.write(r.content)


def comrad_work_schedule(work_queue: Queue):
    print("Spawned new Comrad.")

    session = requests.Session()
    session.headers = {
        "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36",
        "Connection": "Keep-Alive",
        "Referer": "https://www.reddit.com/",
        "Origin": "www.reddit.com",
        "Sec-Fetch-Dest": "image",
        "Sec-Fetch-Mode": "no-cors",
        "Sec-Fetch-Site": "cross-site",
        "Sec-GPC": "1",
        "Accept": "image/avif,image/webp,*/*",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate, br",
        "DNT": "1"
    }

    command = work_queue.get()

    while command is not HaveSomeRestComrade:
        command = work_queue.get()
        if command is HaveSomeRestComrade:
            break

        command: DownloadRequest
        download(download_request=command, session=session)

    print("comrad lived honest and nice")
    work_queue.put(HaveSomeRestComrade)
