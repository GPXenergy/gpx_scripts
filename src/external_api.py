import requests
from requests import HTTPError

from logger import gpx_logger
from power_data import PowerData


class ExternalApi:
    _host: str
    _additional_headers: dict

    def __init__(self, host: str, additional_headers: dict) -> None:
        self._host = host
        self._additional_headers = additional_headers

    def aggregate_data(self, participation_total, participation_client, start) -> PowerData:
        raise NotImplementedError

    def retrieve_data(self, path: str, query_params: dict):
        try:
            return requests.get(self._host + path, query_params, headers=self._additional_headers)
        except HTTPError as e:
            gpx_logger.error(e)
            return e
