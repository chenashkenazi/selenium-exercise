FROM ubuntu:latest
COPY /src /opt
RUN set -xe \
    && apt-get update -y \
    && apt-get install -y python3-pip
RUN pip3 install --upgrade pip
RUN pip3 install -r /opt/requirements.txt
ENV PYTHONPATH /opt
CMD ["python3", "/opt/main.py"]