from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers='10.111.120.19:9092')
for i in range(10):
    print(i)
    future = producer.send('test', b'message')
    result = future.get(timeout=60)
