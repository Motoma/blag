#!/usr/bin/env sh

for SERVER in p0 p1
do
    ssh $SERVER.motoma.io -T -C << EOF
rm -rf stage && mkdir -p stage && cd stage
git clone https://github.com/Motoma/motoma.io.git && cd motoma.io
docker build -t motoma.io .
docker kill blog
docker rm blog
docker run --name blog -d -p 80:80/tcp -t motoma.io
EOF
   
done
