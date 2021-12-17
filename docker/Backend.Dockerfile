FROM cluster-base

ARG spark_version=3.2.0

RUN apt-get update -y && \
    apt-get install -y python3-pip && \
    pip3 install wget pyspark==${spark_version}


ENV   PYTHONUNBUFFERED 1
RUN mkdir /app
COPY backend/requirements.txt /app/
RUN pip3 install --upgrade pip
RUN pip3 install -r app/requirements.txt
COPY . /app
WORKDIR /app
EXPOSE 8000
# RUN python manage.py migrate
# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]