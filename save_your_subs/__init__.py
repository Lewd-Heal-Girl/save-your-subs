from queue import Queue
import logging

from .utils import HaveSomeRestComrade
from .imgur import spawn_imgur_comrades
from .reddit import start_download
from .process_post import Processor
from .generic_hoster import spawn_generic_comrades

logging.basicConfig(
    filename="errors.log",
    filemode='w',
    format=logging.BASIC_FORMAT,
    level=logging.INFO
)


def cli(subreddit: str):
    if not subreddit.startswith("r/"):
        print(f"your sub needs to start with r/: {subreddit}")
        return

    post_queue, reddit_thread_list = start_download(subreddit.replace("r/", "", 1))

    generic_work_queue = spawn_generic_comrades()
    imgur_queue = spawn_imgur_comrades()

    processor = Processor(
        reddit_queue=post_queue,
        imgur_queue=imgur_queue,
        general_queue=generic_work_queue
    )

    def a_thread_is_alive() -> bool:
        nonlocal reddit_thread_list

        some_copy = reddit_thread_list.copy()

        for thread in some_copy:
            if thread.is_alive():
                return True

            reddit_thread_list.remove(thread)

        return False

    while not post_queue.empty() or a_thread_is_alive():
        if post_queue.empty():
            continue

        processor.process(post_queue.get())

    generic_work_queue.put(HaveSomeRestComrade)
    imgur_queue.put(HaveSomeRestComrade)
    print("Terminating the main thread.")
