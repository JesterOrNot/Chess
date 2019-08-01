apt-get update && apt upgrade -y --force-yes \
apt-get install -y apt-utils openjdk-8-jdk ant ca-certificates-java
yarn install
curl -s get.sdkman.io | bash
source ~/.sdkman/bin/sdkman-init.sh
sdk install ant