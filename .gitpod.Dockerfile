FROM gitpod/workspace-full-vnc:branch-jx-python-tk
RUN apt-get update \
    && apt-get install -y libgtk-3-dev
RUN pip2 uninstall pylint --yes
RUN pip3 install pylint