FROM jenkins/inbound-agent:latest

USER root

RUN apt-get update && \
    apt-get install -y docker.io rpm dpkg-dev && \
    apt-get clean

USER jenkins
