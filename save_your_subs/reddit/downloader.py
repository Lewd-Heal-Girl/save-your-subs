from queue import Queue

from time import sleep


def download_subreddit(subreddit: str, result_queue: Queue):
    print("downloading", subreddit)

    for i in range(10):
        result_queue.put(str(i))
        sleep(2)
