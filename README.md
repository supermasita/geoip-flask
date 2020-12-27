# Python Flask GeoLite2 City service
![](https://api.travis-ci.org/supermasita/geoip-flask.svg?branch=master)

## Running
Using Flask only (development):
```
python3 app.py
```

Using UWSGI (example):
```
/usr/local/bin/uwsgi --master --http 0.0.0.0:8888 --chdir /opt/geoip-flask/ --module app:app --processes 4
```

## Usage
* See information of your IP: <https://your-endpoint.com/>
* See information of IP 63.245.208.212: <https://your-endpoint.com/63.245.208.212>
* Get JSON with information of your IP: <https://your-endpoint.com/api/v1.0/ip/>
* Get JSON with information of IP 63.245.208.212: <https://your-endpoint.com/api/v1.0/ip/63.245.208.212>

## Configuration via OS variables
The following OS variables can be set to override `config.py`:
* "GEOIP_DB_LOCATION" ("GeoLite2-City/GeoLite2-City.mmdb")
* "GEOIP_APP_HOST" ("0.0.0.0")
* "GEOIP_APP_PORT" ("8888")
* "GEOIP_APP_DEBUG" (False)
* "GEOIP_APP_DOMAIN" ("geoip.supermasita.com")
* "GEOIP_APP_TITLE" ("A service for MaxMind's GeoIP DB using Flask")

If you are running a Docker image, you can use `docker run -e GEOIP_APP_DOMAIN=example.com ...`.

## Getting updated Maxmind DB
Due to changes in how Maxmind allows to download updated versions of their DBs, ATM there is no built in process to periodically update it. To do so you can rebuild the image passing `--build-arg LICENSE_KEY={your maxmind key}` or download an updated Docker image from [Dockerhub](https://hub.docker.com/r/supermasita/geoip-flask).

## Credits
* We use GeoLite2 data created by [Maxmind](http://www.maxmind.com)
