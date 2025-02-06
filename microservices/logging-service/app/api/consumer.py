from confluent_kafka import Consumer
import asyncio
# from app.db import SessionLocal, AuditLog
import logging
from app.api.db_manager import add_log
from app.api.models import Log

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("my logger")

KAFKA_TOPIC = "service-logs"
KAFKA_BOOTSTRAP_SERVERS = "kafka:9092"
conf = {
    'bootstrap.servers': KAFKA_BOOTSTRAP_SERVERS,
    'auto.offset.reset': 'earliest',
    'group.id': KAFKA_TOPIC,
}

consumer = Consumer(conf)
consumer.subscribe([KAFKA_TOPIC])

def process_log(log_data: Log):
    try:
        add_log(log_data)
        print(f"Logged: {log_data}")
    except Exception as e:
        print(f"Error inserting log into database: {e}")


    # logging.info("in consume logs")

    # async with SessionLocal() as session:
    #     for message in consumer:
    #         log_data = eval(message.value)  # Convert string to dict
    #         log_entry = AuditLog(
    #             service=log_data["service"],
    #             endpoint=log_data["endpoint"],
    #             message=log_data["message"],
    #         )
    #         session.add(log_entry)
    #         await session.commit()

# if __name__ == "__main__":
#     asyncio.run(consume_logs())