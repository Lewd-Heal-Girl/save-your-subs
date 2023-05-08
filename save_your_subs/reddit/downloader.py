import logging
from queue import Queue
import requests

from .classes import Post

LOGGER = logging.getLogger("reddit")

MAX_LIMIT = 100
ENDPOINT = "https://www.reddit.com/r/{subreddit}/new.json?limit={limit}&after={last_id}&count={count}"


def download_subreddit(subreddit: str, result_queue: Queue):
    print("downloading", subreddit)

    session = requests.Session()
    session.headers = {
        "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36",
        "Connection": "Keep-Alive"
    }

    total_posts = 0

    last_id = ''
    limit = MAX_LIMIT

    last_post = None
    while True:
        weird_status_code = False
        data = dict()

        try:
            if last_post is not None:
                last_id = last_post.id

            endpoint = ENDPOINT.format(
                subreddit=subreddit,
                limit=limit,
                last_id=last_id,
                count=total_posts
            )
            
            r = session.get(endpoint)

            if r.status_code != 200:
                weird_status_code = True
                LOGGER.warn(f"reddit respondet with {r.status_code} at: {endpoint}")
            data: dict = r.json()

        except requests.RequestException:
            LOGGER.error(f"Reddit request failed: {endpoint}")

        if data.get("kind") != "Listing":
            LOGGER.warning(f"response type was not 'Listing' {data}")
            continue

        _last_post = last_post

        for post in data.get("data", {}).get("children", []):
            last_post = Post(json=post.get("data", {}))
            print(last_post)
            result_queue.put(last_post)

            total_posts += 1

        if _last_post == last_post and not weird_status_code:
            print("The last Post was reached:")
            print(last_post)
            LOGGER.info(f"{last_post.id}: last post")
            LOGGER.info(f"Total posts: {total_posts}")
            break

    print("Terminating the reddit thread.")
