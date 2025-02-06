from confluent_kafka import Consumer, KafkaError
import json
from fastapi import FastAPI, APIRouter
from app.api.consumer import process_log, consumer
from app.api.db import database
import time 
import logging

# metadata.create_all(engine)
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("my logger")
app = FastAPI(openapi_url="/api/v1/logging/openapi.json", docs_url="/api/v1/logging/docs")

@app.on_event("startup")
async def startup():
    await database.connect()
    try:
        while True:
            msg = consumer.poll(1.0)  # Poll for messages with a timeout of 1 second
            if msg is None:
                continue
            if msg.error():
                if msg.error().code() == KafkaError._PARTITION_EOF:
                    # End of partition event
                    continue
                else:
                    print(f"Kafka error: {msg.error()}")
                    break
            # Decode the message and process the log
            log_data = json.loads(msg.value().decode('utf-8'))
            process_log(log_data)
    except KeyboardInterrupt:
        print("Logging service stopped.")
    finally:
        # Close the Kafka consumer
        consumer.close()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

logging_router = APIRouter()
app.include_router(logging_router, prefix='/api/v1/logging', tags=['logging'])    
