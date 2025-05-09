# Dockerfile for rds_scanner.py app
FROM python:3.9-alpine

RUN pip install boto3

COPY rds_scanner.py /rds_scanner.py

ENTRYPOINT ["python", "/rds_scanner.py"]

