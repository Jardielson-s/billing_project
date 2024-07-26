# Dockerfile

FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
RUN python3 manage.py makemigrations
RUN python3 manage.py migrate

COPY . .

CMD ["gunicorn", "billing_project.wsgi:application", "--bind", "0.0.0.0:8000"]
