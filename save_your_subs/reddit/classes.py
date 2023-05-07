from dataclasses import dataclass
from datetime import datetime
from typing import List, Tuple
from urllib.parse import urlparse
import logging

from slugify import slugify

LOGGER = logging.getLogger("reddit")


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
        return "https://i.redd.it" + parsed.path

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

    def _get_reddit_gallery(self, json: dict):

        media_id_list = [item.get("media_id") for item in self.json.get("gallery_data", dict()).get("items", [])]
        media_metadata = self.json.get("media_metadata", {})

        return [RedditGallery(json=media_metadata.get(str(_id), dict())) for _id in media_id_list]

    @property
    def media(self) -> List[Media]:
        if "url_overridden_by_dest" in self.json:
            url_overridden_by_dest: str = self.json.get("url_overridden_by_dest")
            parsed_url = urlparse(url_overridden_by_dest)

            # check for imgur
            if parsed_url.netloc == "imgur.com" or parsed_url.netloc == "i.imgur.com":
                return [ImgurMedia(url=url_overridden_by_dest)]

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
            if parsed_url.netloc == "i.redd.it":
                return [Media(
                    url=url_overridden_by_dest,
                    id=parsed_url.path.strip("/").split(".")[0]
                )]

        return []

    def __str__(self):
        return f"{self.date} r/{self.subreddit} - {self.title} ({self.flair}) by u/{self.artist}"
