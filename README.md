# lab01-kafka

This laboratory show:

* run Apache Kafka with docker-compose.
* run an Apache Kafka cluster on Kubernetes.  [Strimzi](https://github.com/marcgenerdemiguel/lab01-kafka/blob/main/strimzi)
* Producer and Consumer topics in Apache Kafka.

## Run Apache Kafka with docker-compose.

* [./docker-compose up -d](https://github.com/marcgenerdemiguel/lab01-kafka/blob/main/docker-compose.yml)

## Build client images

* docker build --no-cache -t kafkaproducer-randomnumbers:1.0.0 producer/.
* docker build --no-cache -t kafkaconsumer-randomnumbers:1.0.0 consumer/.

## Run clients

* docker run --env BROKER_IP=kafka --env BROKER_PORT=9093 --env TOPIC_NAME=numbers --network=lab01-kafka_default -it -d --name producer-numbers marcgenerdemiguel/producer-numbers:1.0.0
* docker run --env BROKER_IP=kafka --env BROKER_PORT=9093 --env TOPIC_NAME=numbers --network=lab01-kafka_default -it -d --name consumer-numbers kafkaconsumer-randomnumbers:1.0.0


