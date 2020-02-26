ARG PYTHON_VERSION=3.7

FROM python:${PYTHON_VERSION}

WORKDIR /src

COPY requirements.txt /src/requirements.txt
RUN pip install -r requirements.txt

COPY . /src
CMD pytest