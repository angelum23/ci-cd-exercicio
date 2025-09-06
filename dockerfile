FROM python:3.9-slim

WORKDIR /app

COPY app.py /app
COPY test_app.py /app

RUN pip install --no-cache-dir flask pytest

EXPOSE 5000

CMD ["python", "app.py"]
