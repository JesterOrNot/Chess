#!/bin/bash
export VERSION=`curl -s https://api.github.com/repos/cdr/code-server/releases/latest | grep -oP '"tag_name": "\K(.*)(?=")'`
wget https://github.com/cdr/code-server/releases/download/$VERSION/code-server$VERSION-linux-x64.tar.gz
tar -xvzf code-server$VERSION-linux-x64.tar.gz
cd code-server$VERSION-linux-x64
./code-server --no-auth --port 8080