FROM python:3.11-slim

WORKDIR /code

# Install system deps for MySQL client + cryptography build
RUN apt-get update && apt-get install -y \
    gcc \
    default-libmysqlclient-dev \
    libssl-dev \
    libffi-dev \
    make \
 && rm -rf /var/lib/apt/lists/*

# Install Python deps
COPY app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the source code
COPY ./app ./app
COPY ./scripts ./scripts

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
