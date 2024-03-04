from dataclasses import dataclass, field
from cloudquery.sdk.scheduler import Client as ClientABC

from plugin.observations.client import ObservationsClient

DEFAULT_CONCURRENCY = 100
DEFAULT_QUEUE_SIZE = 10000


@dataclass
class Spec:
    base_url: str = field(default="https://api.example.com")
    family_id: int = field(default=1)
    bbox: object = field(
        default_factory={
            "swlat": 35.530836,
            "swlng": -79.071087,
            "nelat": 36.117908,
            "nelng": -78.247617,
        }
    )
    concurrency: int = field(default=DEFAULT_CONCURRENCY)
    queue_size: int = field(default=DEFAULT_QUEUE_SIZE)


class Client(ClientABC):
    def __init__(self, spec: Spec) -> None:
        self._spec = spec
        self._client = ObservationsClient(spec.base_url, spec.family_id, spec.bbox)

    def id(self):
        return "observations"

    @property
    def client(self) -> ObservationsClient:
        return self._client
