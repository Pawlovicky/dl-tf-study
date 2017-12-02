FROM ubuntu:16.04
MAINTAINER Paul Posch <paulmartinposch@gmail.com>
RUN apt-get update
RUN apt-get install -y python3.5

RUN apt-get install -y python3-pip python3-dev
RUN pip3 install jupyter pandas scikit-learn matplotlib scikit-image
