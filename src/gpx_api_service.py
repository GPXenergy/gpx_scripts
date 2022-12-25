import json

import requests

from power_data import PowerData
from version import version


class GpxApiService:
    _endpoint = 'https://dashboard.gpx.nl/api/meters/measurement/'

    def submit(self, power: PowerData, identifier: str, gpx_key: str, gpx_meter_id: str):
        sn = '%s_%s' % (identifier, gpx_meter_id)
        response = self._post_data({'power': power.as_payload(sn)}, {
            'User-Agent': 'GPXCONN/script-%s' % version,
            'Authorization': 'Token %s' % gpx_key,
        })

        return response.status_code == 201

    def _post_data(self, data: dict, headers: dict):
        return requests.post(self._endpoint, json=data, headers=headers)
