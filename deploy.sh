#!/usr/bin/env sh

for SERVER in p0 p1
do
    ssh $SERVER.motoma.io -T -C << EOF
rm -rf stage && mkdir -p stage && cd stage
git clone https://github.com/Motoma/blag.git && cd blag
docker build -t motoma.io .
docker kill blog
docker run --name blog -d -p 80:80/tcp -t motoma.io
EOF
   
done
