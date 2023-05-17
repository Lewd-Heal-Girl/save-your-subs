from queue import Queue
import logging


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
    
    subreddit = subreddit.strip("r/")
    print(f"propagating r/{subreddit}")
    