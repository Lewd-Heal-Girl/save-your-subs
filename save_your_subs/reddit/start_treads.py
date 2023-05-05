from typing import Tuple
import threading
from queue import Queue

from . import downloader


def start_download(subreddit: str) -> Tuple[Queue, threading.Thread]:
    result_queue = Queue()

    reddit_thread = threading.Thread(target=downloader.download_subreddit, args=(subreddit, result_queue))
    reddit_thread.start()

    return result_queue, reddit_thread
