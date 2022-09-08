import kafka_helper
import time

if __name__ == "__main__":
	consumer = kafka_helper.connect_kafka_consumer(_topic="processed_values_topic")
	while True:
		try:
			for msg in consumer:
				value = msg.value.decode('utf-8')
				print("Received message: " + str(value))
		except Exception as ex:
			msg = "Issue in consuming: {}".format(ex)
			print(msg)
			continue