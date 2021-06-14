import pulsar
from pulsar.schema import *

class WordCount(Record):
    word = String()
    count = Long(required=True)

client = pulsar.Client('pulsar://localhost:6650')

consumer = client.subscribe('my-result-output-topic', 'my-subscription', schema=JsonSchema(WordCount))

while True:
    msg = consumer.receive()
    try:
        print("Received message '{}'".format(msg.data()))
        # Acknowledge successful processing of the message
        consumer.acknowledge(msg)
    except:
        # Message failed to be processed
        consumer.negative_acknowledge(msg)

client.close()
