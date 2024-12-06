FROM python:3.11-slim

WORKDIR /app
COPY . /app/

RUN pip install --no-cache-dir -r requirements.txt

CMD ["gunicorn", "--bind", "0.0.0.0:8080", "plagio_inspector.wsgi:application"]
