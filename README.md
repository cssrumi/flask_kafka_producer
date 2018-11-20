# Quickguide

1. Requirements
docker, docker-compose, git

2. PULL git project
mkdir GIT
cd GIT/
git clone https://github.com/cssrumi/flask_kafka_producer.git

3. Settings:
# Dockerfile
If you are using proxy then add --proxy=ip:port
RUN pip install -r requirements.txt --proxy=ip:port

# docker-compose.yml
set IP of KAFKA_ADVERTISED_HOST_NAME in kafka service:
KAFKA_ADVERTISED_HOST_NAME: ip_adress_of_kafka_cluster
(do not use localhost)

# Global proxy settings if necessary:
will be added in future...

4. Rum
sudo docker-compose up -d

###
Remember to build image :
sudo docker-compose build

To turn off docker:
sudo docker-compose stop

To list containers:
sudo docker container ls

To remove containers:
sudo docker rm <containerid>

To access to container bash:
sudo docker exec -it <containerid> bash
