from typing import List
from pathlib import Path

from ..utils import DATA_PATH, POST_FOLDER_NAME
from .classes import Post


def posts_from_backup(subreddit: str, data_path: Path = DATA_PATH, post_folder_name: str = POST_FOLDER_NAME) -> List[Post]:
    data_path = Path(data_path, subreddit, post_folder_name)
    
    if not data_path.exists():
        print(f"{subreddit} doesn't have a backup: {data_path}")
        