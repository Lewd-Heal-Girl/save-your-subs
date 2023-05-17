from typing import List, Iterable
from pathlib import Path
import json
import pandas as pd
import shutil

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

def get_whole_dataframe(subreddit: str, image_folder: Path) -> pd.DataFrame:
    return pd.DataFrame(post.get_items(
            id=str(i).zfill(4), 
            hosts=[media.url for media in post.media], 
            local_images=[f"{str(i).zfill(4)}_{str(j).zfill(2)}{image.suffix}" for j, image in enumerate(post.images_list)]
        ) for i, post in enumerate(PostIteator(subreddit=subreddit)))


def export(subreddit: str):
    clean = Path(DATA_PATH, subreddit, CLEAN_FOLDER_NAME)
    clean.mkdir(parents=True, exist_ok=True)
    
    image_path = Path(clean, IMAGE_FOLDER_NAME)
    image_path.mkdir(exist_ok=True, parents=True)
    
    print("Saving csv file.")
    get_dataframe(subreddit=subreddit).to_csv(Path(clean, f"{subreddit}.csv"), index=False)
    print("Saving json file.")
    get_whole_dataframe(subreddit=subreddit, image_folder=image_path).to_json(Path(clean, f"{subreddit}.json"))
    
    json_path = Path(clean, POST_FOLDER_NAME)
    json_path.mkdir(exist_ok=True, parents=True)
    
    print("Copying images.")
    for i, post in enumerate(PostIteator(subreddit=subreddit)):
        for j, image in enumerate(post.images_list):
            new_image_path = Path(image_path, f"{str(i).zfill(4)}_{str(j).zfill(2)}{image.suffix}")
            
            shutil.copy(str(image), str(new_image_path))
        
        with Path(json_path, f"{str(i).zfill(4)}.json").open("w") as f:
            json.dump(post.json, f)
        