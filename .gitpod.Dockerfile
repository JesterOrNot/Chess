FROM java:latest
RUN apt-get install \
    apt-utils \
    python3 \
    yarn \
    python3-pip \
    clang \
    nano \
    vim \
    npm \
    nodejs \
RUN pip3 install \
    setuptools \
    googler \
    pygame \