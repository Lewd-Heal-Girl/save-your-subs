from queue import Queue
import requests

from .classes import Post

MAX_LIMIT = 100
ENDPOINT = "https://www.reddit.com/r/{subreddit}/new.json?limit={limit}&after={last_id}"


def download_subreddit(subreddit: str, result_queue: Queue):
    print("downloading", subreddit)

    session = requests.Session()
    session.headers = {
        "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36",
        "Connection": "Keep-Alive"
    }

    last_id = ''
    limit = MAX_LIMIT

    last_post = None

    for i in range(10):
        data = dict()

        try:
            if last_post is not None:
                last_id = last_post.id

            r = session.get(ENDPOINT.format(
                subreddit=subreddit,
                limit=limit,
                last_id=last_id
            ))

            print(r.status_code)
            data: dict = r.json()

        except requests.RequestException:
            print("reddit request failed")

        if data.get("kind") != "Listing":
            continue

        for post in data.get("data", {}).get("children", []):
            last_post = Post(json=post.get("data", {}))
            result_queue.put(last_post)

    print("Terminating the reddit thread.")
