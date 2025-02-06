from confluent_kafka import Producer
import json

# producer_conf = {
#     'bootstrap.servers': 'kafka:29092',
#     'client.id': 'my-app'
# }

# producer = Producer(producer_conf)

# def publish_log(service, endpoint, message):
#     # log = {"service": service, "endpoint": endpoint, "message": message}
#     # data = json.dumps(log).encode('utf-8')
#     producer.produce("service_logs", value="hello")
#     producer.flush()