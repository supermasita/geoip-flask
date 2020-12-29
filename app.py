#!flask/bin/python
from flask import Flask, jsonify, render_template, request
from config import geo_db_location, app_host, app_port, app_debug, app_domain, app_title, app_proxy_ip_header


import geoip2.database
import os.path
import time


app = Flask(__name__)


def _get_requester_ip():
    """Figure out the ip from the request. use `remote_addr` unless a specific header is found
       ('X-Real-IP', by default).
       
       :returns: String (ip)
    """
    if request.headers.get(app_proxy_ip_header):
        return request.headers.get(app_proxy_ip_header)
    else:
        return request.remote_addr


def _get_ip(ip=None):
    """Use passed IP (or figure out IP from request if none passed) to retreive the geo data from
       Maxmind's DB.

       :returns: Dictionary. 
                 Key 'result' will be one of the following:
                 - "SUCCESS"
                 - "NOT_FOUND", when `AddressNotFoundError` is raised (valid IP, but not found in DB)
                 - "ERROR", when `ValueError` is raised (the string you passed is not an IP)
                 - "EXCEPTION", for any other exception
                
    """
    response = {'own_ip': False}
    if ip is None:
        ip = _get_requester_ip()
        response['own_ip'] = True
    response['ip'] = ip
    response['geoip_db_mtime'] = geoip_db_mtime 
    try:
        ip_response = dbReader.city(ip)
        response.update(ip_response.raw)
        response['result'] = "SUCCESS"
        response['result_message'] = None
    except geoip2.errors.AddressNotFoundError as e:
        response['result'] = "NOT_FOUND"
        response['result_message'] = "{}".format(e)
        app.logger.warning(e)
    except ValueError as e:
        response['result'] = "ERROR"
        response['result_message'] = "{}".format(e)
        app.logger.warning(e)
    except Exception as e:
        response['result'] = "EXCEPTION"
        response['result_message'] = "{}".format(e)
        app.logger.exception(e)
    return response


@app.route('/', methods=['GET'])
@app.route('/<string:ip>', methods=['GET'])
def html_response(ip=None, own_ip=False):
    """Get data for IP and render HTML template
    """
    results = _get_ip(ip)
    return render_template("index.html", results=results,
                           app_title=app_title, app_domain=app_domain)


@app.route('/api/v1.0/ip/', methods=['GET'])
@app.route('/api/v1.0/ip/<string:ip>', methods=['GET'])
def json_response(ip=None):
    """Get data for IP and return as JSON
    """
    return jsonify(_get_ip(ip))


if __name__ == '__main__':
    try:
        geoipDbPath = os.path.join(os.path.dirname(__file__), geo_db_location)
        dbReader = geoip2.database.Reader(geoipDbPath)
        geoip_db_mtime = time.ctime(os.path.getmtime(geoipDbPath))
        app.run(debug=app_debug, host=app_host, port=app_port)
    except Exception as e:
        raise e
    finally:    
        dbReader.close()
