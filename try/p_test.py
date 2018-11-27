from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers='10.111.120.19:9092',
                         value_serializer=lambda x: x.encode('UTF-8'))

test_json = '{"user":"test","message":"ątest message"}'
for i in range(10):
    print(i)
    future = producer.send('test', test_json)
    result = future.get(timeout=60)
