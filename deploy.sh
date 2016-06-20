#!/usr/bin/env sh

for SERVER in p0 p1
do
    ssh $SERVER.motoma.io -T -C << EOF
rm -rf stage && mkdir -p stage && cd stage
git clone https://github.com/Motoma/motoma.io.git && cd motoma.io
docker-compose build
docker-compose create
docker-compose start
EOF
   
done
