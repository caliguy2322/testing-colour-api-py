ARG PYTHON_VERSION=3.7
FROM python:${PYTHON_VERSION}
WORKDIR /usr/src
COPY requirements.txt ./requirements.txt
RUN pip install -r requirements.txt
COPY . ./
RUN chmod +x ./start.sh
CMD ["/bin/sh", "start.sh"]