
# Strimzi Kafka Operator

Strimzi provides a way to run an Apache Kafka cluster on Kubernetes. https://strimzi.io/

1.  deploy strimzi kafka operator: https://strimzi.io/blog/2018/11/01/using-helm/
2.  start kafka cluster: kubectl apply -f ./strimzi/my-cluster-kafka.yaml
3.  create kafka topic: kubectl apply -f ./strimzi/numbers-topic.yaml

## External clients

Retrieve the bootstrap address you can use to access the Kafka cluster:

* kubectl get kafka my-cluster -o=jsonpath='{.status.listeners[?(@.type=="external")].bootstrapServers}{"\n"}'

start external app kafka producer:

* python3 ./producer/KafkaProducer.py <IP K8s API> <port> <topic>
* python3 ./producer/KafkaProducer.py 10.0.2.15 30166 numbers

Start external app kafka consumer:

* python3 ./producer/KafkaConsumer.py <IP K8s API> <port> <topic>
* python3 ./producer/KafkaConsumer.py 10.0.2.15 30166 numbers
