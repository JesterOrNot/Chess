FROM ubuntu:latest
# Setup JAVA_HOME -- useful for docker commandline
USER root
ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64/
RUN export JAVA_HOME
RUN add-apt-repository ppa:webupd8team/java
RUN \
  apt-get update && \
  apt upgrade -y --force-yes && apt-get -y install \
    apt-utils \
    openjdk-8-jdk \
    ant \
    ca-certificates-java \
    clang \
    zsh \