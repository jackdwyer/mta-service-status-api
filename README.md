# mta-service-status-api
Provides an API wrapper around the MTA status page: [MTA Status](http://tripplanner.mta.info/mobileApps/serviceStatus/serviceStatusPage.aspx?mode=subway)

## Usage
```bash
$ curl http://mta-status.dwyer.club
{
  "data": {
    "1": "PLANNED WORK",
    "2": "PLANNED WORK",
    "3": "PLANNED WORK",
    "4": "PLANNED WORK",
    "5": "PLANNED WORK",
    "6": "PLANNED WORK",
    "7": "GOOD SERVICE",
    "A": "DELAYS",
    "B": "DELAYS",
    "C": "DELAYS",
    "D": "DELAYS",
    "E": "DELAYS",
    "F": "DELAYS",
    "G": "GOOD SERVICE",
    "J": "GOOD SERVICE",
    "L": "PLANNED WORK",
    "M": "DELAYS",
    "N": "DELAYS",
    "Q": "DELAYS",
    "R": "DELAYS",
    "S": "GOOD SERVICE",
    "SIR": "GOOD SERVICE",
    "W": "DELAYS",
    "Z": "GOOD SERVICE"
  },
  "last_updated": "Mon, 29 May 2017 20:36:47 GMT"
}
```
[http://mta-status.dwyer.club](http://mta-status.dwyer.club)


## Installation
```bash
$ git clone git@github.com:jackdwyer/mta-service-status-api.git
$ docker-compose up
$ curl localhost:5000
```
