from dataclasses import dataclass
from pathlib import Path

from .reddit import Media

class HaveSomeRestComrade:
    pass

@dataclass
class DownloadRequest:
    media: Media
    folder: Path
    n: int