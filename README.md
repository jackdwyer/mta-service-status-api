# mta-service-status-api
Provides an API wrapper around the MTA status page: [MTA Status](http://tripplanner.mta.info/mobileApps/serviceStatus/serviceStatusPage.aspx?mode=subway)

## Usage
```bash
$ curl http://mta-status.dwyer.club
{
  "data": {
    "123": "PLANNED WORK",
    "456": "PLANNED WORK",
    "7": "GOOD SERVICE",
    "ACE": "PLANNED WORK",
    "BDFM": "PLANNED WORK",
    "G": "GOOD SERVICE",
    "JZ": "GOOD SERVICE",
    "L": "PLANNED WORK",
    "NQR": "PLANNED WORK",
    "S": "GOOD SERVICE",
    "SIR": "GOOD SERVICE"
  },
  "last_updated": "Mon, 29 May 2017 13:41:14 GMT"
}
```
[http://mta-status.dwyer.club](http://mta-status.dwyer.club)


## Installation
```bash
$ git clone git@github.com:jackdwyer/mta-service-status-api.git
$ docker-compose up
$ curl localhost:5000
```
