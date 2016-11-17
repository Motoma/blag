FROM nginx

MAINTAINER Christopher Gilbert <motoma@gmail.com>

EXPOSE 80/tcp

ADD ./www /usr/share/nginx/html
RUN chmod a+r -R /usr/share/nginx/html
