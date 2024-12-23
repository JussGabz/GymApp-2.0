FROM python:3.9
ENV PYTHONUNBUFFERED 1
WORKDIR /app
RUN sudo chown -R $(whoami):$(whoami) /home/***/app/postgres
COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt
COPY . /app/
RUN python manage.py collectstatic --noinput

