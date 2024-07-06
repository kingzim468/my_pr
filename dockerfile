FROM jenkins/jenkins:lts

USER root

RUN apt-get update && \
    apt-get install -y docker.io && \
    chmod 666 /var/run/docker.sock

USER jenkins