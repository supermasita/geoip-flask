# docker run -d --network="web" -p 8888:8888  --name="geoip" -t geoip

FROM ubuntu:18.04

ENV UPDATED "2019-02-27"

RUN apt-get update && apt-get install -y gnupg

RUN echo "deb http://ppa.launchpad.net/maxmind/ppa/ubuntu bionic main" >> /etc/apt/source.list

RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys F44B38CE3DB1BF64B61DBD28DE1997DCDE742AFA 

RUN apt-get update \
    && apt-get install -y git python3-pip curl unzip cron geoipupdate supervisor 

RUN cd /opt/ \
    && curl https://codeload.github.com/supermasita/geoip-flask/zip/master -o master.zip \
    && unzip master.zip \
    && mv geoip-flask-master geoip-flask \
    && rm -f master.zip

RUN cd /opt/geoip-flask && pip3 install -r requirements.txt

RUN mkdir /opt/geoip-flask/GeoLite2-City/ \ 
    && /usr/bin/geoipupdate -d /opt/geoip-flask/GeoLite2-City/

COPY geoipupdate.cron /etc/cron.d/geoipupdate

COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf 

EXPOSE 8888 9191

CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/conf.d/supervisord.conf"]
