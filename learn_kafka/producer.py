import json
import uuid
from confluent_kafka import Producer

producer_config = {
    'bootstrap.servers': 'localhost:9092'
}

producer = Producer(producer_config)

order = {
    'order_id': str(uuid.uuid4()),
    'user': 'tesyept',
    'item': 'hahahah',
    'quantity': 1
}

value = json.dumps(order).encode('utf-8')

def delivery_report(err, msg):
    if err:
        print(f'Delivery failed: {err}')
    else:
        print(f'Delivered {msg.value().decode('utf-8')}')
        print(f'key: {msg.key()}, offset: {msg.offset()}, partition: {msg.partition()}, topic: {msg.topic()}')
    print(dir(msg))

producer.produce(
    topic='orders', 
    value=value,
    callback=delivery_report)

producer.flush()