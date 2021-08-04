# Run example:
#  sudo docker run -d --env GEOIP_APP_ENDPOINT=http://example.com:8888 -p 8888:8888  -t supermasita/geoip-flask
# Build with:
#  --build-arg LICENSE_KEY={your maxmind key}

FROM ubuntu:20.04

ENV UPDATED "2020-12-30"

ARG LICENSE_KEY

RUN apt-get update \
    && apt-get install -y python3-pip curl unzip supervisor 

RUN cd /opt/ \
    && curl https://codeload.github.com/supermasita/geoip-flask/zip/master -o master.zip \
    && unzip master.zip \
    && mv geoip-flask-master geoip-flask \
    && rm -f master.zip

RUN cd /opt/geoip-flask \
    && pip3 install -r requirements.txt

RUN mkdir /opt/geoip-flask/GeoLite2-City/

RUN curl "https://download.maxmind.com/app/geoip_download?edition_id=GeoLite2-City&license_key=${{ secrets.LICENSE_KEY }}&suffix=tar.gz" \ 
    -o /opt/geoip-flask/GeoLite2-City/GeoLite2-City.tar.gz 

RUN cd /opt/geoip-flask/GeoLite2-City \ 
    && tar xvf /opt/geoip-flask/GeoLite2-City/GeoLite2-City.tar.gz --strip 1 \ 
    && rm -f /opt/geoip-flask/GeoLite2-City/GeoLite2-City.tar.gz 

COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf 

EXPOSE 8888 9191

CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/conf.d/supervisord.conf"]
