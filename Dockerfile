FROM continuumio/miniconda3
MAINTAINER hamraa

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY ./requirements.txt ./
RUN conda update -n base -c defaults conda
RUN conda install -y --file requirements.txt
COPY . .
