# lab01-kafka

* docker build --no-cache -t kafkaproducer-randomnumbers:1.0.0 producer/.
* docker build --no-cache -t kafkaconsumer-randomnumbers:1.0.0 consumer/.

* ./docker-compose up -d

* docker run --env BROKER_IP=kafka --env BROKER_PORT=9093 --env TOPIC_NAME=numbers --network=lab01-kafka_default -it -d --name producer-numbers kafkaproducer-randomnumbers:1.0.0
* docker run --env BROKER_IP=kafka --env BROKER_PORT=9093 --env TOPIC_NAME=numbers --network=lab01-kafka_default -it -d --name consumer-numbers kafkaconsumer-randomnumbers:1.0.0

