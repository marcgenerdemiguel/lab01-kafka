from json import dumps
from kafka import KafkaProducer
from random import random
import sys

ip_broker = sys.argv[1]
port = sys.argv[2]
server = ip_broker + ':' + port
topic = sys.argv[3]

producer = KafkaProducer(bootstrap_servers=[server],
                         value_serializer=lambda x:
                         dumps(x).encode('utf-8'))
while True:
    number = round(random()*1000000)
    data = {'number' : number}
    print(data)
    producer.send(topic, value=data)
