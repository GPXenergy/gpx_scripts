import argparse
import datetime
import logging

from api_outsmart import ApiOutSmart
from gpx_api_service import GpxApiService
from logger import gpx_logger

parser = argparse.ArgumentParser(
    prog='GPX remote connector',
    description='Retrieve power data from remote APIs to send to GPX servers'
)

parser.add_argument('-i', '--identifier', help='Name of this producer, e.g. windparkkoningspleij', type=str, required=True)
parser.add_argument('-a', '--api', help='type of remote api of producer', choices=['outsmart'], type=str, required=True)
parser.add_argument('-k', '--api_key', help='API key for remote api', type=str, required=True)
parser.add_argument('-pt', '--participation_total', help='Total participation for this producer, e.g. 10600', default=1, type=int)
parser.add_argument('-pc', '--participation_client', help='Participation owned by the client, e.g. 1', default=1, type=int)
parser.add_argument('-s', '--start', help='Start date for kWh data, e.g. 2022-04-20', type=str, required=True)
parser.add_argument('-g', '--gpx_key', help='API key for gpx api', type=str, required=True)
parser.add_argument('-gi', '--gpx_meter_id', help='API key for gpx api', type=str, required=True)

args = parser.parse_args()


def validate_args():
    assert datetime.date.fromisoformat(args.start) <= datetime.date.today(), 'Date must be in past'


if __name__ == '__main__':
    validate_args()

    # TODO make configurable with args
    fh = logging.FileHandler('../gpx_script.log')
    fh.setLevel(logging.ERROR)
    gpx_logger.addHandler(fh)

    identifier = args.identifier
    api = args.api
    api_key = args.api_key
    participation_total = args.participation_total
    participation_client = args.participation_client
    start = args.start
    gpx_key = args.gpx_key
    gpx_meter_id = args.gpx_meter_id

    if api == 'outsmart':
        remote_service = ApiOutSmart(api_key)
    else:
        raise ValueError('api not supported:', api)

    data = remote_service.aggregate_data(
        participation_total,
        participation_client,
        start,
    )

    if data:
        gpx_service = GpxApiService()
        success = gpx_service.submit(
            data,
            identifier,
            gpx_key,
            gpx_meter_id,
        )
        gpx_logger.debug('submission %s' % ('Success' if success else 'Failure'))
