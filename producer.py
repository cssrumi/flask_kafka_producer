import json
from time import sleep
from kafka import KafkaProducer


class Producer:
    def __init__(self, **kwargs):
        self.kafka_param = dict()
        # self.kafka_param['bootstrap_servers'] = ['10.111.120.132:9092']
        self.kafka_param['bootstrap_servers'] = 'localhost:9092'

        for key, value in kwargs.items():
            self.kafka_param[key] = value
        print(self.kafka_param['bootstrap_servers'])
        self.producer = KafkaProducer(
            bootstrap_servers=self.kafka_param['bootstrap_servers'],
            value_serializer=lambda x: json.dumps(x).encode('utf-8'),
        )

    def _parse_json(self, json_dict):
        message = json_dict
        if message.get('topic', None):
            topic = message['topic']
            del message['topic']
        else:
            topic = 'test'
        # message = json.dumps(message).encode('utf-8')
        return topic, message

    def _send_to_topic(self, topic, message):
        print('message:', message, '\ttype:', type(message), '\ttopic:', topic)
        future = self.producer.send(topic, value=message)
        result = future.get(timeout=60)

    def send(self, json_dict):
        topic, message = self._parse_json(json_dict)
        self._send_to_topic(topic, message)
