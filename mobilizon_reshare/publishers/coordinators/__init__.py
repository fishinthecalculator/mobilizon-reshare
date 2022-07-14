import logging
from dataclasses import dataclass
from typing import Optional, Sequence

from mobilizon_reshare.models.publication import PublicationStatus


@dataclass
class BasePublicationReport:
    status: PublicationStatus
    reason: Optional[str]

    @property
    def succesful(self):
        return self.status == PublicationStatus.COMPLETED

    def get_failure_message(self):
        return (
            f"Publication failed with status: {self.status}.\n" f"Reason: {self.reason}"
        )


@dataclass
class BaseCoordinatorReport:
    reports: Sequence[BasePublicationReport]

    @property
    def successful(self):
        return all(r.status == PublicationStatus.COMPLETED for r in self.reports)


logger = logging.getLogger(__name__)
