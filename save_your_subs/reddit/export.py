from typing import List, Iterable
from pathlib import Path
import json

from ..utils import DATA_PATH, POST_FOLDER_NAME, IMAGE_FOLDER_NAME
from .classes import Post


class PostIteator:
    def __init__(self, subreddit: str, data_path: Path = DATA_PATH, post_folder_name: str = POST_FOLDER_NAME):
        self.subreddit = subreddit
        
        self.data_path = Path(data_path, subreddit, post_folder_name)
        
        if not self.data_path.exists():
            print(f"{subreddit} doesn't have a backup: {data_path}")

    def __iter__(self):
        if not self.data_path.exists():
            return
        
        
        for post_file in self.data_path.glob("*.json"):
            with post_file.open("r") as f:
                yield Post(json=json.load(f), data_path=Path(DATA_PATH, self.subreddit, IMAGE_FOLDER_NAME))
        