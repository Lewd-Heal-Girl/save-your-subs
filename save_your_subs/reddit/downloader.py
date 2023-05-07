from queue import Queue
import requests

from .classes import Post

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
        data = dict()

        try:
            if last_post is not None:
                last_id = last_post.id

            r = session.get(ENDPOINT.format(
                subreddit=subreddit,
                limit=limit,
                last_id=last_id,
                count=total_posts
            ))

            print(r.status_code)
            data: dict = r.json()

        except requests.RequestException:
            print("reddit request failed")

        if data.get("kind") != "Listing":
            continue

        _last_post = last_post

        for post in data.get("data", {}).get("children", []):
            last_post = Post(json=post.get("data", {}))
            print(last_post)
            result_queue.put(last_post)

            total_posts += 1

        if _last_post == last_post:
            print("The last Post was reached:")
            print(last_post)
            print(last_post.id)
            print(f"total posts: {total_posts}")
            break

    print("Terminating the reddit thread.")
