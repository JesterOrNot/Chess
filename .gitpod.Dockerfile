FROM gitpod/workspace-full-vnc
RUN apt-get update \
    && apt-get install -y libgtk-3-dev
RUN export VERSION=`curl -s https://api.github.com/repos/cdr/code-server/releases/latest | grep -oP '"tag_name": "\K(.*)(?=")'`
RUN wget https://github.com/cdr/code-server/releases/download/$VERSION/code-server$VERSION-linux-x64.tar.gz
RUN tar -xvzf code-server$VERSION-linux-x64.tar.gz
WORKDIR code-server$VERSION-linux-x64
RUN ./code-server --no-auth --port 8080
EXPOSE 8080
EXPOSE 3000
EXPOSE 3306
EXPOSE 5000
