from dataclasses import dataclass
from pathlib import Path
from urllib.parse import ParseResult

from .reddit import Media


class HaveSomeRestComrade:
    pass


@dataclass
class DownloadRequest:
    id_: str
    media: Media
    folder: Path
    n: int


IMAGE_EXTENSIONS = {'jpg', 'jpeg', 'jpe', 'jif', 'jfif', 'jfi', 'png', 'gif', 'webp', 'tiff', 'tif', 'psd', 'raw',
                    'bmp', 'heif', 'heic', 'indd', 'ai', 'eps'}


def url_is_image(parsed_url: ParseResult) -> bool:
    path = parsed_url.path.lower()

    path = path.strip("/")
    filename = path[-1]

    # getting the file extension by splitting by "." and "?"
    extension = filename.split(".", 1)[-1].split("?")[0].strip()

    return extension in IMAGE_EXTENSIONS
