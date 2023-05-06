from dataclasses import dataclass
from pathlib import Path

from ..reddit import Media

@dataclass
class DownloadRequest:
    media: Media
    folder: Path
    n: int
