FROM gitpod/workspace-full-vnc
RUN apt-get update \
    && apt-get install -y libgtk-3-dev
EXPOSE 3000
EXPOSE 3306
EXPOSE 5000
