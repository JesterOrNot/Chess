FROM gitpod/workspace-full
USER root
RUN sudo apt-get update \
 && sudo apt-get install -y \
    apt-utils yarn ant python3 python3-pip clang nano vim zsh python3-venv \
 && sudo rm -rf /var/lib/apt/lists/*
RUN pip3 install \
    setuptools matplotlib sympy numpy \