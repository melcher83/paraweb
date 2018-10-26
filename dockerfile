FROM python:3.7


CMD ["/bin/bash"]


RUN mkdir /config
ADD requirements.txt /config
RUN pip3 install -r /config/requirements.txt

RUN mkdir /src

WORKDIR /src

EXPOSE 8000