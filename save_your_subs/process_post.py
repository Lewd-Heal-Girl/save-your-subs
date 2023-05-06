from pathlib import Path
import json
from queue import Queue

from .reddit import Post
from .generic_hoster import DownloadRequest

DATA_PATH = Path("subs-stashed-away")


class Processor:
    def __init__(
            self,
            reddit_queue: Queue,
            imgur_queue: Queue,
            general_queue: Queue,
            data_path: Path = DATA_PATH
    ):
        self.reddit_queue = reddit_queue
        self.imgur_queue = imgur_queue
        self.general_queue: Queue = general_queue

        self.data_path = data_path

    def process(self, post: Post):
        sub_path = Path(self.data_path, post.subreddit)
        sub_path.mkdir(parents=True, exist_ok=True)

        post_path = Path(sub_path, "posts")
        post_path.mkdir(parents=True, exist_ok=True)

        image_path = Path(sub_path, "images", post.folder)
        image_path.mkdir(parents=True, exist_ok=True)

        with Path(post_path, f"{post.id}.json").open("w") as f:
            json.dump(post.json, f, indent=4)

        print(post, len(post.media))
        for i, media in enumerate(post.media):
            self.general_queue.put(DownloadRequest(
                media=media,
                n=i,
                folder=image_path
            ))
            print("\t", media.url, media.resolution)
