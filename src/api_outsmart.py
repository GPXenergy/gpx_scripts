import datetime

import pytz

from external_api import ExternalApi
from logger import gpx_logger
from power_data import PowerData


class ApiOutSmart(ExternalApi):
    def __init__(self, api_key: str) -> None:
        if not api_key:
            raise ValueError('api_key cannot be empty')

        host = 'https://wpm.out-smart.eu'
        headers = {
            'Authorization': 'Bearer %s' % api_key,
        }
        super().__init__(host, headers)

    def aggregate_data(self, participation_total, participation_client, start):
        mw_response = self.retrieve_data(
            '/Bazefield.Services/api/measurements/timeseries',
            {
                'keys': 'PLE-CALC-ActivePowerMW',
                'Interval': '1s',
                'From': '*-5s',
                'To': '*',
                'format': 'json',
            }
        )
        mwh_response = self.retrieve_data(
            '/Bazefield.Services/api/measurements/timeseries/aggregated',
            {
                'keys': 'PLE-PI-ProducedMWh',
                'Aggregates': 'SUM',
                'Interval': '12M',
                'From': start,
                'To': '*',
                'format': 'json',
            }
        )
        mw_data = mw_response.json()
        mwh_data = mwh_response.json()

        return self.extract_power_data(mw_data, mwh_data, participation_total, participation_client)

    def extract_power_data(self, mw_data, mwh_data, participation_total, participation_client) -> PowerData or None:
        try:
            mw = mw_data['timeSeriesList'][0]['timeSeries'][-1]['v'] if len(mw_data['timeSeriesList'][0]['timeSeries']) else 0
            mwh = mwh_data['timeSeriesList'][0]['timeSeries'][0]['v']
            if not mwh:
                gpx_logger.debug('No mwh data')
                return None
            if mw:
                timestamp = mw_data['timeSeriesList'][0]['timeSeries'][-1]['t_local']
            else:
                timestamp = datetime.datetime.now(pytz.timezone('Europe/Amsterdam')).isoformat()
            export_1 = (mwh * 1000) * (participation_client / participation_total)
            actual_export = (mw * 1000) * (participation_client / participation_total)
            return PowerData(
                timestamp=timestamp,
                export_1='%.3f' % export_1,
                actual_export='%.3f' % actual_export,
            )
        except IndexError as e:
            gpx_logger.error(e)
            raise e
