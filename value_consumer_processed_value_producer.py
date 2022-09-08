import kafka_helper
import time

if __name__ == "__main__":
	consumer = kafka_helper.connect_kafka_consumer(_topic="raw_values_topic")
	producer = kafka_helper.connect_kafka_producer()
	## continuosly consuming data from raw-values-topic process them and publish processed data to processed_values_topic
	while True:
		try:
			for msg in consumer:
				value = msg.value.decode('utf-8')
				print("Received message: " + str(value))
				updated_value = int(value)*int(value)
				value_type = "Odd"
				if int(value)%2 > 0:
					continue
				value_type = "Even"
				kafka_helper.publish_message(producer, "processed_values_topic", value_type, value)
		except Exception as ex:
			msg = "Issue in consuming: {}".format(ex)
			print(msg)
