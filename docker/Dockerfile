# Run example:
#    ```
#    sudo docker run -d --env GEOIP_APP_ENDPOINT=http://example.com:8888 -p 8888:8888  -t supermasita/geoip-flask
#    ```
# 
# Building instructions:
# 1. Download GeoIP DB to current path:
#    ```
#    curl "https://download.maxmind.com/app/geoip_download?edition_id=GeoLite2-City&license_key={YOUR_LICENSE_KEY}&suffix=tar.gz" --output ./GeoLite2-City.tar.gz
#    ```
# 2. Build with (example):
#    ```
#    sudo docker build --tag "supermasita/geoip-flask" .
#    ```
# 

FROM ubuntu:latest

ENV UPDATED "2024-03-13"

RUN apt-get update \
    && apt-get install -y python3-pip curl unzip supervisor 

RUN cd /opt/ \
    && curl https://codeload.github.com/supermasita/geoip-flask/zip/master -o master.zip \
    && unzip master.zip \
    && mv geoip-flask-master geoip-flask \
    && rm -f master.zip

RUN cd /opt/geoip-flask \
    && pip3 install -r requirements.txt

COPY GeoLite2-City.tar.gz /opt/geoip-flask/GeoLite2-City/

RUN cd /opt/geoip-flask/GeoLite2-City \ 
    && tar xvf /opt/geoip-flask/GeoLite2-City/GeoLite2-City.tar.gz --strip 1 \ 
    && rm -f /opt/geoip-flask/GeoLite2-City/GeoLite2-City.tar.gz 

COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf 

EXPOSE 8888 9191

CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/conf.d/supervisord.conf"]
