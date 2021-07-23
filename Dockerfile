FROM python:3.7.6

WORKDIR /root

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update

COPY . .

RUN pip install --upgrade pip

RUN pip install -r requirements.txt
RUN pip install gunicorn

RUN find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
RUN find . -path "*/migrations/*.pyc"  -delete