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
        print(f"Logged in process: {log_data}")
        add_log(log_data)
    except Exception as e:
        print(f"Error inserting log into database (process step): {e}")
