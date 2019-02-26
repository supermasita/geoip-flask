#!flask/bin/python
from flask import Flask, jsonify, render_template, request

import geoip2.database
import os.path
import time

# from datetime import datetime, timedelta

# DB location
geoipDbPath = os.path.join(os.path.dirname(
    __file__), 'GeoLite2-City/GeoLite2-City.mmdb')


app = Flask(__name__)


def get_geo(remote_ip):
    dbReader = geoip2.database.Reader(geoipDbPath)
    try:
        response = dbReader.city(remote_ip)
        return response
    except (Exception, geoip2.errors.AddressNotFoundError) as e:
        raise e
    finally:
        dbReader.close()


@app.route('/', methods=['GET'])
@app.route('/<string:ip>', methods=['GET'])
def index(ip=None, own_ip=False):
    if ip is None:
        own_ip = True
        if request.headers.get('X-Real-IP'):
            ip = request.headers.get('X-Real-IP')
        else:
            ip = request.remote_addr
    results = get_ip(ip)
    results = results.json
    results['ip'] = ip
    results['own_ip'] = own_ip
    return render_template("index.html", results=results)


@app.route('/api/v1.0/ip/', methods=['GET'])
def get_ip_own():
    if request.headers.get('X-Real-IP'):
        ip = request.headers.get('X-Real-IP')
    else:
        ip = request.remote_addr
    response = get_ip(ip)
    return response


@app.route('/api/v1.0/ip/<string:ip>', methods=['GET'])
def get_ip(ip):
    try:
        ip_response = get_geo(ip)
        response = ip_response.raw
        response['geoip_DB_MTime'] = time.ctime(os.path.getmtime(geoipDbPath))
    except (ValueError, geoip2.errors.AddressNotFoundError) as e:
        response = {"error": "{}".format(e)}
    return jsonify(response)


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=8888)
