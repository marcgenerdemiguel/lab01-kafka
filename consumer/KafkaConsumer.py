from kafka import KafkaConsumer
from json import loads
import sys

ip_broker = sys.argv[1]
port = sys.argv[2]
server = ip_broker + ':' + port
topic = sys.argv[3]

consumer = KafkaConsumer(topic, bootstrap_servers=[server],
                         auto_offset_reset='earliest', enable_auto_commit=True, group_id='group-numbers',
                         value_deserializer=lambda x: loads(x.decode('utf-8')))

for message in consumer:
    message = message.value
    print(message)
