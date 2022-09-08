from kafka import KafkaProducer
import kafka_helper
import time
import random

if __name__ == "__main__":
    producer = kafka_helper.connect_kafka_producer()
    ## here I consider this infinite loop as stream that continuously publish data to raw-values-topic
    while True:
        i = random.randint(0, 10000)
        kafka_helper.publish_message(producer, "raw_values_topic", "raw-value", str(i))
        # time.sleep(3)