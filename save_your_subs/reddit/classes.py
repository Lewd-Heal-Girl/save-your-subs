from dataclasses import dataclass
from datetime import datetime
from typing import List, Tuple
from urllib.parse import urlparse
import logging
import re
from pathlib import Path

from slugify import slugify

from ..utils import url_is_image

LOGGER = logging.getLogger("reddit")
MARKDOWN_PATTERN = r"\[.*?\]\((.*?)\)"




class Media:
    def __init__(
            self,
            id: str = None,
            url: str = None,
            resolution: Tuple[int, int] = None
    ):
        self._id: str = id
        self._url: str = url
        self._resolution: True[int, int] = resolution or (0, 0)

    @property
    def id(self) -> str:
        return self._id

    @property
    def url(self) -> str:
        return self._url

    @property
    def resolution(self) -> Tuple[int, int]:
        return self._resolution


class RedditGallery(Media):
    def __init__(self, json: dict):
        super().__init__()
        self.json: dict = json

    @property
    def id(self):
        return self.json.get("id")

    @property
    def url(self) -> str:
        parsed = urlparse(self.json.get("s", dict()).get("u"))
        return "https://i.redd.it" + str(parsed.path)

    @property
    def resolution(self) -> Tuple[int, int]:
        return self.json.get("s", dict()).get("x"), self.json.get("s", dict()).get("y")


class MediaPreview(Media):
    def __init__(self, json: dict):
        super().__init__()
        self.json: dict = json

    @property
    def id(self) -> str:
        return self.json.get("id")

    @property
    def url(self) -> str:
        return self.json.get("source", dict()).get("url")

    @property
    def resolution(self) -> Tuple[int, int]:
        return self.json.get("source", dict()).get("width", 0), self.json.get("source", dict()).get("height", 0)


class ImgurMedia(Media):
    @property
    def id(self) -> str:
        url_frag = self.url.strip("/").split("/")[-1]
        return url_frag.split(".")[0]


@dataclass
class Post:
    json: dict
    data_path: Path = None

    @property
    def url(self) -> str:
        return "https://www.reddit.com" + self.json.get("permalink")

    @property
    def subreddit(self) -> str:
        return self.json.get("subreddit")

    @property
    def title(self) -> str:
        return self.json.get("title")

    @property
    def id(self):
        return self.json.get("name")

    @property
    def flair(self) -> str:
        return self.json.get("link_flair_text")

    @property
    def date(self) -> datetime:
        return datetime.fromtimestamp(int(self.json.get("created", 0)))

    @property
    def artist(self) -> str:
        return self.json.get("author")

    @property
    def folder(self) -> str:
        return slugify(f"{self.id} {self.title}")[:254]

    @property
    def image_path(self) -> Path:
        return Path(self.data_path, self.folder)
    
    @property
    def images_list(self) -> List[Path]:
        return list(self.image_path.glob("*"))
    
    @property
    def image_count(self) -> int:
        return len(self.images_list)

    def _get_reddit_gallery(self, json: dict):
        media_id_list = []
        
        gallery_data = json.get("gallery_data", {})
        if gallery_data is None:
            return []
        
        
        for item in gallery_data.get("items", list()):
            if item is None:
                continue
            media_id_list.append(item.get("media_id"))
            
        media_metadata = json.get("media_metadata", {})

        return [RedditGallery(json=media_metadata.get(str(_id), dict())) for _id in media_id_list]

    def _parse_url(self, url: str) -> List[Media]:
        parsed_url = urlparse(url)

        # check for imgur
        if parsed_url.netloc == "imgur.com" or parsed_url.netloc == "i.imgur.com":
            return [ImgurMedia(url=url)]

        # check for reddit gallery
        if "reddit" in parsed_url.netloc and parsed_url.path.startswith("/gallery"):
            r = self._get_reddit_gallery(self.json)
            if len(r) > 0:
                return r

            for crosspost in self.json.get("crosspost_parent_list", list()):
                r = self._get_reddit_gallery(crosspost)
                if len(r) > 0:
                    return r

        # check for single reddit post (ez)
        if parsed_url.netloc == "i.redd.it" and url_is_image(parsed_url):
            return [Media(
                url=url,
                id=parsed_url.path.strip("/").split(".")[0]
            )]

        # check for any other image hoster
        if url_is_image(parsed_url):
            return [Media(
                url=url,
                id=None
            )]

        return []

    def _media_from_text(self, markdown: str) -> List[Media]:
        r = []
        for url_match in re.findall(MARKDOWN_PATTERN, markdown):
            r.extend(self._parse_url(url=url_match))

        return r

    @property
    def media(self) -> List[Media]:
        # getting the pictures in actual picture posts
        if "url_overridden_by_dest" in self.json:
            url_overridden_by_dest: str = self.json["url_overridden_by_dest"]
            r = self._parse_url(url_overridden_by_dest)
            if len(r) > 0:
                return r

        # scanning the text of text post for valid links
        if "selftext" in self.json:
            markdown: str = self.json["selftext"]

            r = self._media_from_text(markdown)
            if len(r) > 0:
                return r

            for crosspost in self.json.get("crosspost_parent_list", list()):
                r = self._media_from_text(crosspost.get("selftext", ""))
                if len(r) > 0:
                    return r

        return []

    def __str__(self):
        return f"{self.date} r/{self.subreddit} - {self.title} ({self.flair}) by u/{self.artist}"

    def get_items(self, **kwargs) -> dict:
        return {
            'subreddit': self.subreddit,
            'title': self.title,
            'artist': self.artist,
            'flair': self.flair,
            'url': self.url,
            **kwargs,
            'images': self.image_count,
            'reddit_id': self.id
        }
