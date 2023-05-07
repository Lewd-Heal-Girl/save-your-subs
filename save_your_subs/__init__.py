from queue import Queue

from .utils import HaveSomeRestComrade
from .imgur import spawn_imgur_comrades
from .reddit import start_download
from .process_post import Processor


def cli(subreddit: str):
    if not subreddit.startswith("r/"):
        print(f"your sub needs to start with r/: {subreddit}")
        return

    post_queue, reddit_thread = start_download(subreddit.replace("r/", "", 1))

    generic_work_queue = Queue()
    imgur_queue = spawn_imgur_comrades()

    processor = Processor(
        reddit_queue=post_queue,
        imgur_queue=imgur_queue,
        general_queue=generic_work_queue
    )

    while not post_queue.empty() or reddit_thread.is_alive():
        if post_queue.empty():
            continue

        processor.process(post_queue.get())

    generic_work_queue.put(HaveSomeRestComrade)
    imgur_queue.put(HaveSomeRestComrade)
    print("Terminating the main thread.")
