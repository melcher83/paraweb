FROM python:3.6


CMD ["/bin/bash"]


RUN mkdir /config
ADD requirements.txt /config
RUN pip3 install -r /config/requirements.txt
RUN apt-get update
RUN apt-get install graphviz

RUN mkdir /src

WORKDIR /src

EXPOSE 8000