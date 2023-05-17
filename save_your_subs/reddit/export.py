from typing import List, Iterable
from pathlib import Path
import json
import pandas as pd

from ..utils import DATA_PATH, POST_FOLDER_NAME, IMAGE_FOLDER_NAME, CLEAN_FOLDER_NAME
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
        
def get_dataframe(subreddit: str) -> pd.DataFrame:
    return pd.DataFrame(post.get_items(id=str(i).zfill(4)) for i, post in enumerate(PostIteator(subreddit=subreddit)))

def export(subreddit: str):
    clean = Path(DATA_PATH, subreddit, CLEAN_FOLDER_NAME)
    clean.mkdir(parents=True, exist_ok=True)
    
    get_dataframe(subreddit=subreddit).to_csv(Path(clean, f"{subreddit}.csv"), index=False)
        