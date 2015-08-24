FROM nginx

MAINTAINER Christopher Gilbert <motoma@gmail.com>

EXPOSE 80/tcp

ADD ./www /usr/share/nginx/html
ADD ./www_root /usr/share/nginx/html
ADD /static /usr/share/nginx/html/static
RUN chmod a+r -R /usr/share/nginx/html
