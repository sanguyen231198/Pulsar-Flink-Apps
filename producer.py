import pulsar

client = pulsar.Client('pulsar://localhost:6650')
producer = client.create_producer('my-input-topic')
producer.send(('hello pulsar hello hello pulsar hello world').encode('utf-8'))

client.close()
