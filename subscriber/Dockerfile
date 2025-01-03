FROM python:3.10-slim

WORKDIR /app

COPY subscriber/ .

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python3", "subscriber.py"]