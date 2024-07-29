FROM python:3.10-slim

WORKDIR /app

ENV PYTHONUNBUFFERED=1

COPY requirements.txt ./

RUN pip install -r requirements.txt

RUN python manage.py collectstatic --noinput

RUN echo "from django.contrib.auth import get_user_model; User = get_user_model(); \
if not User.objects.filter(username='${DJANGO_SUPERUSER_USERNAME}').exists(): \
    User.objects.create_superuser('${DJANGO_SUPERUSER_USERNAME}', '${DJANGO_SUPERUSER_EMAIL}', '${DJANGO_SUPERUSER_PASSWORD}')" \
| python manage.py shell

COPY . .

CMD ["gunicorn", "main.wsgi:application", "--bind", "0.0.0.0:8000"]
