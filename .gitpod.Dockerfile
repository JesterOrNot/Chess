FROM gitpod/workspace-full-vnc:branch-jx-python-tk
RUN apt-get update \
    && apt-get install -y libgtk-3-dev
EXPOSE 8080
EXPOSE 3000
EXPOSE 3306
EXPOSE 5000
