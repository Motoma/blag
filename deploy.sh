#!/usr/bin/env sh

tar -czf static.tgz static

cd www
tar -czf ../www.tgz *

cd ..
scp *.tgz web1.motoma.io:
rm static.tgz www.tgz

ssh web1.motoma.io -T -C << EOF
mkdir -p ~/backup
mv /var/www/motoma.io ~/backup/`date -Iminutes`
mkdir -p /var/www/motoma.io
tar -zxf www.tgz -C /var/www/motoma.io
tar -zxf static.tgz -C /var/www/motoma.io
mv /var/www/motoma.io/static/favicon.ico /var/www/motoma.io/
mv /var/www/motoma.io/static/robots.txt /var/www/motoma.io/
mv /var/www/motoma.io/static/motoma.asc /var/www/motoma.io/
rm static.tgz www.tgz
EOF
