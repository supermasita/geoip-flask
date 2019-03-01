# Python Flask GeoLite2 City service
![](https://api.travis-ci.org/supermasita/geoip-flask.svg?branch=master)

## Demo/Usage
* See information of your IP: <https://geoip.supermasita.com/>
* See information of IP 63.245.208.212: <https://geoip.supermasita.com/63.245.208.212>
* Get JSON with information of your IP: <https://geoip.supermasita.com/api/v1.0/ip/>
* Get JSON with information of IP 63.245.208.212: <https://geoip.supermasita.com/api/v1.0/ip/63.245.208.212>

## Running
Using Flask only (development):
```
python3 app.py
```

Using UWSGI:
```
/usr/local/bin/uwsgi --master --http 0.0.0.0:8888 --chdir /opt/geoip-flask/ --module app:app --processes 4
```

## Credits
* We use GeoLite2 data created by [Maxmind](http://www.maxmind.com)
