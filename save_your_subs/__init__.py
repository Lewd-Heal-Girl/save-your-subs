from .reddit import start_download


def cli(subreddit: str):
    if not subreddit.startswith("r/"):
        print(f"your sub needs to start with r/: {subreddit}")
        return

    post_queue, reddit_thread = start_download(subreddit.replace("r/", "", 1))

    while not post_queue.empty() or reddit_thread.is_alive():
        if post_queue.empty():
            continue

        print(post_queue.get())

    print("ending main thread")
