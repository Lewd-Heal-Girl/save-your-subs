import logging
from queue import Queue
import requests
import threading

from .classes import Post
from ..utils import HaveSomeRestComrade

LOGGER = logging.getLogger("reddit")


MAX_LIMIT = 100


class RedditComrade(threading.Thread):
    def __init__(self, subreddit: str, endpoint_queue: Queue, result_queue: Queue):
        self.subreddit = subreddit
        self.endpoint_queue = endpoint_queue
        self.result_queue = result_queue

        self.session = requests.Session()
        self.session.headers = {
            "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36",
            "Connection": "Keep-Alive"
        }

        threading.Thread.__init__(self)

    def fetch_endpoint(self, endpoint: str, limit: int = MAX_LIMIT):
        total_posts = 0

        last_id = ''

        last_post = None
        while True:
            weird_status_code = False
            data = dict()

            if last_post is not None:
                last_id = last_post.id

            url = endpoint.format(
                subreddit=self.subreddit,
                limit=limit,
                last_id=last_id,
                count=total_posts
            )

            try:
                r = self.session.get(url)

                if r.status_code != 200:
                    weird_status_code = True
                    LOGGER.warning(f"reddit responded with {r.status_code} at: {url}")
                data: dict = r.json()

            except requests.RequestException:
                LOGGER.error(f"Reddit request failed: {url}")

            if data.get("kind") != "Listing":
                LOGGER.warning(f"response type was not 'Listing' {data}")
                continue

            _last_post = last_post

            for post in data.get("data", {}).get("children", []):
                last_post = Post(json=post.get("data", {}))
                print(last_post)
                self.result_queue.put(last_post)

                total_posts += 1

            if _last_post == last_post and not weird_status_code:
                print("The last Post was reached:")
                LOGGER.info(str(last_post))
                LOGGER.info(f"{last_post.id}: last post")
                LOGGER.info(f"Total posts: {total_posts}")
                break

    def run(self) -> None:
        command = self.endpoint_queue.get()

        while command is not HaveSomeRestComrade:
            command = self.endpoint_queue.get()
            if command is HaveSomeRestComrade:
                break

            command: str
            self.fetch_endpoint(endpoint=command)

        # tell another worker to rest
        self.endpoint_queue.put(HaveSomeRestComrade)
