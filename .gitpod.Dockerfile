FROM ubuntu:latest
# Setup JAVA_HOME -- useful for docker commandline
USER root
ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64/
RUN export JAVA_HOME
RUN add-apt-repository ppa:webupd8team/
RUN apt update
RUN export VER="1.10.5"
RUN apt install -y wget vim
RUN wget https://www-eu.apache.org/dist//ant/binaries/apache-ant-${VER}-bin.tar.gz
RUN tar -xvf apache-ant-${VER}-bin.tar.gz -C /usr/local
RUN ln -s /usr/local/apache-ant-${VER}/ /usr/local/ant
RUN vim /etc/profile.d/ant.sh
RUN export ANT_HOME=/usr/local/ant
RUN export PATH=${PATH}:${ANT_HOME}/bin
RUN source /etc/profile.d/ant.sh
RUN echo $ANT_HOME
RUN echo $PATH
RUN \
  apt-get update && \
  apt upgrade -y --force-yes && apt-get -y install \
    apt-utils \
    openjdk-8-jdk \
    ant \
    ca-certificates-java \
    clang \
    zsh \