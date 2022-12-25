# gpx_scripts

usage:
```
GPX remote connector [-h] -i IDENTIFIER -a {outsmart} -k API_KEY
                     [-pt PARTICIPATION_TOTAL] [-pc PARTICIPATION_CLIENT] -s
                     START -g GPX_KEY -gi GPX_METER_ID
```

Retrieve power data from remote APIs to send to GPX servers

arguments:
* `-h, --help`
    * show this help message and exit
* `-i IDENTIFIER, --identifier IDENTIFIER`
    * Name of this producer, e.g. windparkkoningspleij
* `-a REMOTE_API, --api REMOTE_API`
    * type of remote api of producer, options: {outsmart}
* `-k API_KEY, --api_key API_KEY`
    * API key for remote api
* `-pt PARTICIPATION_TOTAL, --participation_total PARTICIPATION_TOTAL`
    * Total participation for this producer, e.g. 10600
* `-pc PARTICIPATION_CLIENT, --participation_client PARTICIPATION_CLIENT`
    * Participation owned by the client, e.g. 1
* `-s START, --start START`
    * Start date for kWh data, e.g. 2022-04-20
* `-g GPX_KEY, --gpx_key GPX_KEY`
    * API key for gpx api
* `-gi GPX_METER_ID, --gpx_meter_id GPX_METER_ID`
    * Unique ID for the meter
