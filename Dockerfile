FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .

COPY . /app

RUN useradd -m appuser

RUN chown -R appuser /app

USER appuser

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD ["python3", "web-server.py"]
