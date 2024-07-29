FROM python:3.10-slim

WORKDIR /app

ENV PYTHONUNBUFFERED=1

COPY requirements.txt ./

RUN pip install -r requirements.txt

RUN python manage.py collectstatic --no-input

COPY . .

CMD ["gunicorn", "main.wsgi:application", "--bind", "0.0.0.0:8000"]
