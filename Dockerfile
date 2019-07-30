FROM gitpod/workspace-full
USER root
RUN apt-get update && apt-get install -y \
        apt-utils yarn ant python3 python3-pip python3-venv \
    && apt-get clean && rm -rf /var/cache/apt/* && rm -rf /var/lib/apt/lists/* && rm -rf /tmp/*
RUN pip3 install \
        setuptools matplotlib sympy numpy
