FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /src
COPY requirements.txt /src
WORKDIR /src
RUN pip install -r requirements.txt
