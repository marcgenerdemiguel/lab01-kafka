FROM python:3
RUN pip install kafka-python
ADD KafkaProducer.py /
ENV BROKER_IP=localhost
ENV BROKER_HOST=9093
ENV TOPIC_NAME=test
CMD python ./KafkaProducer.py $BROKER_IP $BROKER_HOST $TOPIC_NAME

