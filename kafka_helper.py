from kafka import KafkaProducer
from kafka import KafkaConsumer

def connect_kafka_producer(_bootstrap_servers=['localhost: 9092']):
	_producer = None
	try:
		_producer = KafkaProducer(bootstrap_servers=_bootstrap_servers)
		msg = "Successfully connected with Kafka Producer"
		print(msg)
	except Exception as ex:
		msg = "Issue in connecting Kafka Producer: {}".format(ex)
		print(msg)
	finally:
		return _producer

def connect_kafka_consumer(_topic, _auto_offset_reset='earliest',
	_bootstrap_servers=['localhost: 9092'], _consumer_timeout_ms=1000):
	_consumer = None
	try:
		_consumer = KafkaConsumer(_topic, auto_offset_reset=_auto_offset_reset,
			bootstrap_servers=_bootstrap_servers,
			consumer_timeout_ms=_consumer_timeout_ms)
		msg = "Successfully connected with Kafka consumer"
		print(msg)
	except Exception as ex:
		msg = "Issue in connecting with Kafka Consumer: {}".format(ex)
		print(msg)
	finally:
		return _consumer

def publish_message(_producer, _topic, _key, _value):
	try:
		key = bytes(_key, encoding="utf-8")
		value = bytes(_value, encoding="utf-8")
		_producer.send(topic=_topic, key=key, value=value)
		_producer.flush()
		print("Successfully publish the message to topic: {} with key {}".format(_topic, key))
	except Exception as ex:
		msg = "Issue in publishing message to topic: {}".format(ex)
		print(msg)