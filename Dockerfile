FROM python:3.8
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
RUN apt-get update
RUN apt-get install -y iputils-ping
EXPOSE 5500
CMD ["python", "bitbucket.py"]