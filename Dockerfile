FROM python:3.7-alpine

RUN pip install boto3
ADD object-downloader.py /