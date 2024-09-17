FROM python:alpine

LABEL org.opencontainers.image.source=https://github.com/volkovskiyda/docker-speedtest

RUN python -m pip install --upgrade pip
RUN pip install speedtest-cli

COPY ./speedtest.py .
COPY ./run.sh .

CMD ["/bin/sh", "./run.sh"]
