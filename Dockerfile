FROM python:3-alpine
RUN pip install boto3 botocore
COPY demo.py /code/demo.py
WORKDIR /code
ENTRYPOINT [ "python", "/code/demo.py" ]

