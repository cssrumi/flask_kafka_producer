from kafka import KafkaConsumer

consumer = KafkaConsumer('test',
                         bootstrap_servers=['10.111.120.19:9092'],
                         auto_offset_reset='earliest',
                         enable_auto_commit=True,
                         # group_id='my-group',
                         )

for message in consumer:
    print(message.value)
