import os 

# Location of the MMDB
geo_db_location = os.getenv("GEOIP_DB_LOCATION", "GeoLite2-City/GeoLite2-City.mmdb")
# IP where the app listens - 0.0.0.0 for all
app_host = os.getenv("GEOIP_APP_HOST", "0.0.0.0")
# Port where the app listens
app_port = os.getenv("GEOIP_APP_PORT", "8888")
# Flask debug flag
app_debug = os.getenv("GEOIP_APP_DEBUG", False)

# Domain used in template anchors
app_domain = os.getenv("GEOIP_APP_DOMAIN", "geoip.supermasita.com")
# HTML title for template
app_title = os.getenv("GEOIP_APP_TITLE", "A service for MaxMind's GeoIP DB using Flask")

# If behind a proxy, header to look for instead of REMOTE ADDRESS 
app_proxy_ip_header = os.getenv("GEOIP_APP_PROXY_IP_HEADER", "X-Real-IP")

