from confluent_kafka import Producer
import json

producer_conf = {
    'bootstrap.servers': 'kafka:9092',
}
producer = Producer(producer_conf)

def publish_log(service, endpoint, message):
    log = {"service": service, "endpoint": endpoint, "message": message}
    # producer.produce("service-logs", json.dumps(log).encode("utf-8"))
    producer.produce("service-logs", "hello")
    producer.flush()