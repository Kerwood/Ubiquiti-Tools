FROM ubuntu

MAINTAINER Patrick Kerwood @ LinuxBloggen.dk

ENV DEBIAN_FRONTEND noninteractive

COPY DiscoverUbiquiti.py setInform.py INSTRUCTIONS.sh /root/

RUN apt-get update \
	&& apt-get install -y --force-yes python python-dev python-pip nmap \
	&& pip install paramiko pycrypto ecdsa

RUN echo "sh /root/INSTRUCTIONS.sh" >> /root/.bashrc

WORKDIR /root

CMD ["/bin/bash"]
