#!/usr/bin/env sh
tar -czvf static.tgz static
cd www
tar -czvf ../www.tgz *
cd ..
scp *.tgz web1.motoma.io:
ssh web1.motoma.io -C "mkdir -p ~/backup; mv /var/www/motoma.io ~/backup/`date -Iminutes`; mkdir -p /var/www/motoma.io; tar -zxvf www.tgz -C /var/www/motoma.io; tar -zxvf static.tgz -C /var/www/motoma.io; mv /var/www/motoma.io/static/favicon.ico /var/www/motoma.io; rm static.tgz www.tgz"
rm static.tgz www.tgz