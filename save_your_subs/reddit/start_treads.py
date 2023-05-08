from typing import Tuple, List
import threading
from queue import Queue

from .downloader import RedditComrade
from ..utils import HaveSomeRestComrade


COMRADE_COUNT = 4

ENDPOINT_LIST = [
    "https://www.reddit.com/r/{subreddit}/new.json?limit={limit}&after={last_id}&count={count}",
    "https://www.reddit.com/r/{subreddit}/top.json?limit={limit}&after={last_id}&count={count}&t=all",
    "https://www.reddit.com/r/{subreddit}/controversial.json?limit={limit}&after={last_id}&count={count}&t=all",
    "https://www.reddit.com/r/{subreddit}/hot.json?limit={limit}&after={last_id}&count={count}",
    "https://www.reddit.com/r/{subreddit}/top.json?limit={limit}&after={last_id}&count={count}&t=year",
    "https://www.reddit.com/r/{subreddit}/controversial.json?limit={limit}&after={last_id}&count={count}&t=year",
    "https://www.reddit.com/r/{subreddit}/top.json?limit={limit}&after={last_id}&count={count}&t=month",
    "https://www.reddit.com/r/{subreddit}/controversial.json?limit={limit}&after={last_id}&count={count}&t=month",
    "https://www.reddit.com/r/{subreddit}/top.json?limit={limit}&after={last_id}&count={count}&t=week",
    "https://www.reddit.com/r/{subreddit}/controversial.json?limit={limit}&after={last_id}&count={count}&t=week",
    "https://www.reddit.com/r/{subreddit}/top.json?limit={limit}&after={last_id}&count={count}&t=day",
    "https://www.reddit.com/r/{subreddit}/controversial.json?limit={limit}&after={last_id}&count={count}&t=day",
    "https://www.reddit.com/r/{subreddit}/top.json?limit={limit}&after={last_id}&count={count}&t=hour",
    "https://www.reddit.com/r/{subreddit}/controversial.json?limit={limit}&after={last_id}&count={count}&t=hour",
]


def start_download(subreddit: str, reddit_comrades: COMRADE_COUNT) -> Tuple[Queue, List[threading.Thread]]:
    endpoint_queue = Queue()
    for endpoint in ENDPOINT_LIST:
        endpoint_queue.put(endpoint)
    endpoint_queue.put(HaveSomeRestComrade)

    result_queue = Queue()

    threads: List[threading.Thread] = list()

    for i in range(reddit_comrades):
        reddit_thread = RedditComrade(
            subreddit=subreddit,
            endpoint_queue=endpoint_queue,
            result_queue=result_queue
        )
        threads.append(reddit_thread)
        reddit_thread.start()

    return result_queue, threads
