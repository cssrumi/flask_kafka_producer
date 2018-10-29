from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers='localhost:9092')
for i in range(1):
    print(i)
    future = producer.send('test', b'message')
    # result = future.get(timeout=60)
