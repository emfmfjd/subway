
from confluent_kafka import Consumer, KafkaException

def kafka_consumer_function():
    conf = {
        'bootstrap.servers': '192.168.0.209:9092,192.168.0.211:9092,192.168.0.208:9092',
        'group.id': 'airflowconsumer',
        'auto.offset.reset': 'earliest'
    }
    consumer = Consumer(conf)

    def print_assignment(consumer, partitions):
        print('Assignment:', partitions)

    consumer.subscribe(['subway'], on_assign=print_assignment)

    try:
        while True:
            msg = consumer.poll(timeout=1.0)
            if msg is None:
                continue
            if msg.error():
                if msg.error().code() == KafkaError._PARTITION_EOF:
                    continue
                else:
                    raise KafkaException(msg.error())
            print('Received message: {}'.format(msg.value().decode('utf-8')))
    except KeyboardInterrupt:
        pass
    finally:
        consumer.close()

if __name__ == "__main__":
    kafka_consumer_function()