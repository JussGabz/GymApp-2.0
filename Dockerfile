FROM python:3.9
ENV PYTHONUNBUFFERED 1
WORKDIR /app
RUN chown -R ec2-user:ec2-user /home/ec2-user/app/postgre
COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt
COPY . /app/
RUN python manage.py collectstatic --noinput

