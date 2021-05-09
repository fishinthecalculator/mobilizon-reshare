from dataclasses import dataclass, asdict
from datetime import datetime
from enum import Enum
from typing import Optional

from jinja2 import Template


class PublicationStatus(Enum):
    WAITING = 1
    FAILED = 2
    PARTIAL = 3
    COMPLETED = 4


@dataclass
class MobilizonEvent:
    """Class representing an event retrieved from Mobilizon."""

    name: str
    description: str
    begin_datetime: datetime
    end_datetime: datetime
    last_accessed: datetime
    mobilizon_link: str
    mobilizon_id: str
    thumbnail_link: Optional[str] = None
    location: Optional[str] = None
    publication_time: Optional[datetime] = None
    publication_status: PublicationStatus = PublicationStatus.WAITING

    def __post_init__(self):
        assert self.begin_datetime < self.end_datetime
        if self.publication_time:
            assert self.publication_status in [
                PublicationStatus.COMPLETED,
                PublicationStatus.PARTIAL,
            ]

    def _fill_template(self, pattern: Template) -> str:
        return pattern.render(**asdict(self))

    def format(self, pattern: Template) -> str:
        return self._fill_template(pattern)