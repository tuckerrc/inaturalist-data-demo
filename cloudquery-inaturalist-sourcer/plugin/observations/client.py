from typing import Generator, Dict, Any
import math
import requests
from requests.compat import urljoin


class ObservationsClient:
    def __init__(
        self,
        base_url="https://api.inaturalist.org",
        family_id=7823,
        bbox={
            "swlat": 35.530836,
            "swlng": -79.071087,
            "nelat": 36.117908,
            "nelng": -78.247617,
        },
    ):
        self._base_url = base_url
        self._family_id = family_id
        self._swlat = bbox["swlat"]
        self._swlng = bbox["swlng"]
        self._nelat = bbox["nelat"]
        self._nelng = bbox["nelng"]

    def observation_iterator(
        self, page: int = 1
    ) -> Generator[Dict[str, Any], None, None]:
        query = "v1/observations?taxon_id={family_id}&order=desc&order_by=created_at&per_page=200&nelat={nelat}&nelng={nelng}&swlat={swlat}&swlng={swlng}&page={page_num}"
        response = requests.get(
            urljoin(
                self._base_url,
                query.format(
                    family_id=self._family_id,
                    page_num=1,
                    nelat=self._nelat,
                    nelng=self._nelng,
                    swlat=self._swlat,
                    swlng=self._swlng,
                ),
            )
        )
        if response.status_code != 200:
            raise ValueError("Bad HTTP Response")
        data = response.json()
        results = data["results"]
        total_results = data["total_results"]
        per_page = data["per_page"]
        page_count = math.ceil(total_results / per_page)
        page = 1
        while page <= page_count:
            page += 1
            for result in results:
                yield result

            response = requests.get(
                urljoin(
                    self._base_url,
                    query.format(
                        family_id=self._family_id,
                        page_num=page,
                        nelat=self._nelat,
                        nelng=self._nelng,
                        swlat=self._swlat,
                        swlng=self._swlng,
                    ),
                )
            )
            if response.status_code != 200:
                raise ValueError("Bad HTTP Response")
            data = response.json()
            results = data["results"]
