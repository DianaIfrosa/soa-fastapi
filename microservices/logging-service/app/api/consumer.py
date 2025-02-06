from confluent_kafka import Consumer
import asyncio
# from app.db import SessionLocal, AuditLog
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("my logger")

KAFKA_TOPIC = "service_logs"
KAFKA_BOOTSTRAP_SERVERS = "kafka:29092"
conf = {
    'bootstrap.servers': 'kafka:29092',
    'auto.offset.reset': 'earliest',
    'enable.auto.commit': True,
    'group.id': 'my-group',
    'api.version.request': True,
    'api.version.fallback.ms': 0
}

async def consume_logs():
    consumer = Consumer(conf)
    consumer.subscribe(['my-topic'])
    logging.info("in consume logs")

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